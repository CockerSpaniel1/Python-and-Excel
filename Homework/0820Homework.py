import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib.pyplot as plt

#header = 跟伺服器說 你(客戶端)是誰, 要做什麼
header = {  "X-Requested-With":"XMLHttpRequest", # <-少這個就不會回傳資料
            "Referer": "https://ojt.wda.gov.tw/HistoryClassSearch",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} #偽裝成瀏覽器
  
#payload = 網頁搜尋表單內的值
payload = { 'CLASSCNAME': '爬蟲', #<- 要查的內容
            'PlanType': 1,'p': '1-100-103','psize': 100, 'rid':'HistoryClassSearch',
            'STDATE': '2008/02/01 00:00:00', 'STDATE_MON': 2, 'STDATE_YEAR': 2008, 'STDATE_YEAR_SHOW': 97, 
            'FTDATE': '2024/08/31 23:59:59', 'FTDATE_MON': 8, 'FTDATE_YEAR': 2024, 'FTDATE_YEAR_SHOW': 113,
            'IsHisSearch': 'Y', }

try:
    res = requests.post("https://ojt.wda.gov.tw/HistoryClassSearch", headers = header, data = payload)
    data_dict = res.json() # Response物件內的方法 .json(), 另一種寫法  json.loads(res.text) <-參數放字串
    
    print("爬蟲抓取成功 將取得的JSON格式字串轉成字典")
except:
    with open("data.json" ,"r",encoding="utf-8") as rf:
        data_dict = json.load(rf)  # json.load(rf) 參數放檔案
        
    print("爬蟲抓取失敗 改使用JSON檔案讀進資料")
finally:
    print("---------------------------------------------------------------------------------")

#BeautifulSoup區塊-----------------------------------------------------------
#整理來自爬蟲或檔案的json資料 篩選出要的欄位資料並移除HTML標籤
result =  BeautifulSoup(data_dict['Result'], "html.parser")

tr_tags = result.find_all("tr")
data = []
for tr in tr_tags:
    td_tags = tr.find_all("td")
    row_data = []
    i=1
    for td in td_tags:
        if i in range(1,5):
            if i == 2:
                row_data.append( td.text[:td.text.rfind("第")] )
            else:
                row_data.append(td.text)
        #合併學科及術科的訓練地點(只佔用一欄位) 哪個有值就寫入誰 若兩個都有 則先寫5, 寫6的時候在覆蓋5
        elif i in (5,6) and td.text != "":      
            try:
                #覆蓋原本的值
                row_data[4] = td.text
            except IndexError:
                row_data.insert(4, td.text)
        #將起迄日期分割成兩個字串, 轉成西元格式在append到串列上
        elif i == 8:
            #"107/08/06|107/09/07" => ["107/08/06","107/09/07"]
            date = td.text.strip().split("|")[0]
            temp_list = date.split('/')                          #["107/08/06" => ["107","08","06"]
            year_AD = str( int(temp_list[0])+1911 )              # str( int("107") +1911)
            temp_list[0] = year_AD                               #[year_AD ,"08","06"] 
            date_AD = "/".join(temp_list)                        #["2018","08","06"] => "2018/08/06"
            row_data.append(date_AD)

        i +=1 
        
    data.append(row_data)

#DataFrame區塊--------------------------------------------------------------------------------
#將data [[1],[2].[3]] 轉成DataFrame
df1 = pd.DataFrame(data, columns=['訓練單位名稱', '訓練班別', '訓練人數','訓練時數','訓練地點','開始日期'])
#最後三筆用字典建立DataFrame
df2 =pd.DataFrame({ "訓練單位名稱":['社團法人中華民國數位科技推廣協會','國立臺北商業大學','中華民國全競利促進協會'],
                    '訓練班別':['Python 大數據網路爬蟲應用班','Python財經數據爬蟲與分析實務班', 'ChatGPT 暨 Excel VBA 網路爬蟲應用班'],
                    '訓練人數':[25,30,20],
                    '訓練時數':[24,30,54],
                    '訓練地點':['臺中市','臺北市','新竹縣'],
                    '開始日期':['2024/08/06','2024/08/10','2024/08/24'],},index=[1,2,3] )

df = pd.concat([df1,df2], ignore_index=True)
df[['訓練人數','訓練時數']] = df[['訓練人數','訓練時數']].apply(pd.to_numeric) #轉成int型別

df['開始日期'] = pd.to_datetime(df['開始日期'] , format='%Y/%m/%d') #轉成datetime型別

print("資料查詢的時間區間為 2008年2月 到 2024年8月")
print(f"總共有 {df.shape[0]} 門名稱含有爬蟲的課程")
print("第一門爬蟲課程開課時間為 %s" % df.loc[0,'開始日期'].strftime('%Y年%m月%d日'))

rank_city = df['訓練地點'].value_counts().head(3)
print("開課數前三名的城市:" , end=" ")
for i in range(3):
    print(f"{i+1}.{rank_city.index[i]}: {rank_city.iloc[i]}門   ", end="" )
print("")

most_institution = df['訓練單位名稱'].mode()[0] #找到最多次的訓練單位 #另一種寫法 df['訓練單位名稱'].value_counts().head(1)
inst_df = df[df['訓練單位名稱'] == most_institution]  #取得該訓練單位的DF
print("開課數最多的單位: %s的 '%s'  總共開了 %d門課" % (inst_df.iloc[0,4], most_institution, inst_df['訓練班別'].count()) )

most_class = df['訓練班別'].value_counts().head(1)
print("該單位所開的 '%s' 也是最多次的 總共開了 %d次 " % (most_class.index[0], most_class.iloc[0]) )

print("最長的課程時數為 %d小時 最短的課程時數為 %d小時"% ( df['訓練時數'].max(), df['訓練時數'].min()) )
print("大多數的課程時數為 %d小時  平均時數則為 %d小時" % ( df['訓練時數'].mode().iloc[0], df['訓練時數'].mean()) )

h1 = df[ df['開始日期'].dt.month<=6 ].count().loc['訓練班別'] 
h2 = df[ df['開始日期'].dt.month> 6 ].count().iloc[1]

print("在上半年開課有 %d門課  在下半年開課則有 %d門課" % (h1, h2))

df3 = df['訓練班別'].groupby(by=df['開始日期'].dt.year).count()
df4 = df[ df['訓練地點']=="高雄市" ].loc[:,'訓練班別'].groupby(by=df['開始日期'].dt.year).count()

df5 = df3.sort_values(ascending=False)
print("於 %d年開設最多課程 總共開了 %d門課 "% (df5.index[0], df5.iloc[0]) )
print("其次為 %d年  一共開了 %d門課 "% (df5.index[1], df5.iloc[1]) )

#畫圖區塊--------------------------------------------------------------------------------
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.figure(figsize=(8,6)) #設定畫布大小
plt.plot(df3, linewidth=3, label="全台", color='dodgerblue' , marker="h")
plt.plot(df4, linewidth=3, label="高雄", color='salmon'     , marker="D")

plt.title('各年度爬蟲課程', fontsize=16)
plt.xlabel('年'      , fontsize=14, color='cornflowerblue')
plt.ylabel('課程數量', fontsize=14, color='cornflowerblue')

plt.legend( loc='upper left') #圖例的位置
plt.tick_params(axis='both',labelsize=12)
plt.axis([2017.5, 2024.5, 0, 30.7])

plt.grid() #網格
plt.show()