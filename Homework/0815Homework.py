import requests 
from bs4 import BeautifulSoup
import csv
import time

#由於是先用Jupyter notebook撰寫 所以程式碼排列是由功能執行順序分成區塊 (可以避免一直發Requests) 
#1.抓取維基百科的犬種列表 (第一個Requests)
#2.使用BeautifulSoup找出欄位 用2個List存放: [[狗的英文名，中文名，種類，原產地，圖片網址],...]
#3.將data寫入CSV建立檢索表  writerows([[],...])
#4.建立查閱檢索表的函式 ex 輸入:柯基  回傳>正確的品種名:威爾斯柯基犬(資料型態:List)
#5.建立函式爬取子頁面 抓取狗的{別名，身高，體重，壽命}(資料型態:Dictionary)(第二個Requests)
#6.建立類別彙整來自 CSV檔(List) 跟 爬取子頁面的資料(Dictionary)的資料
#7.建立實體物件，並將物件放入陣列(List)中
#8.將物件的屬性值取出，用"""長字串"""寫成HTML網頁標籤的格式
#9.傳入HTML標籤和CSS,JS語法的參數後輸出網頁檔案

#1.抓取維基百科的犬種列表 
url = "https://zh.wikipedia.org/zh-tw/%E7%8A%AC%E7%A8%AE%E5%88%97%E8%A1%A8"

res = requests.get(url )
soup = BeautifulSoup(res.text, "html.parser")

#2.使用BeautifulSoup找出欄位 用2個List存放: [[狗的英文名，中文名，種類，原產地，圖片網址],...]
table_tag = soup.find("table", class_="wikitable") 
tr_tags = table_tag.find_all("tr")

data = []
for tr in tr_tags[1:110]:
    td_tags =tr.find_all("td")
    
    i=1
    row_data = []
    for td in td_tags:
        #print(i, td)
        #以下為整理各欄位的資料 (清除括號或移除部分文字後取得該列每一欄位的資料)  
        if i==1:
            index = td.text.rfind("（")
            text = td.text[:index]
        elif i==2:
            index = td.text.rfind("[")
            text = td.text[:index]
        elif i == 3:
            i+=1
            continue
        elif i==5:
            text = td.text.replace("原產地：","")
        elif i == 6:
            img_tag = td.find("img")
            img_url = img_tag.get("src")
            text = "https:"+img_url
        else:
            text = td.text
        i+=1  
        row_data.append(text.strip())
        
    data.append(row_data)
    

#3.將data寫入CSV建立檢索表  writerows([[],...])
with open(".\\Doggypedia.csv",'w',newline='',  encoding='utf-8-sig') as wf:
        w=csv.writer(wf)
        w.writerows(data) #寫全部 writerows()參數放[['a','b',..],[],]   寫單筆 writerow 參數放['a','b',...]
        print('犬基百科建立成功')

#4.建立查閱檢索表的函式 ex 輸入:柯基  回傳>正確的品種名:威爾斯柯基犬(資料型態:List)
def query(name):
    with open(".\\Doggypedia.csv",'r',newline='',  encoding='utf-8-sig') as rf:    
        data = []
        for row in csv.reader(rf):
            if name in row[1]:
                data.append(row)
    #若輸入 "獵犬" 會有許多筆資料，以下使用Input手動選擇           
    if len(data)>1:
        str = ""
        for i in range(len(data)):
            str += (f"{i+1}:{data[i][1]} ")   
        index = int(input(f"請輸入數字選擇 {str}"))
        data[0] = data[index - 1]

    return data[0]

#5.建立函式爬取子頁面 抓取狗的{別名，身高，體重，壽命}(資料型態:Dictionary)(第二個Requests)
def get_dog_info(dogname):
    url = f"https://zh.wikipedia.org/zh-tw/{dogname}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    dog_dict ={}
    try:
        #以下為整理各欄位的資料 依照特定的條件(欄位標題)取得欄位內容並移除文字前後的空白和後面的[]
        for tr in soup.select(".infobox")[0].find("tbody").find_all("tr", recursive=False):
            ###使用 recursive=False 只會搜尋下一層，避免拿到重複的結果
            th_tags = tr.find_all("th")
            for th in th_tags:
                if th.text in ["別名","壽命"]:
                    th_text = th.text
                    td_text = th.find_next_sibling("td").text.strip()
                    #當find("[") 找不到時回傳 -1 , !=-! >有找到
                    if td_text.find("[") != -1:
                        td_text = td_text[:td_text.find("[")]
                    
                elif  th.text in ["體重","身高"]:
                    th_text = th.text
                    
                    td_tags = th.find_next_siblings("td")
                    for td in td_tags:
                        td_text = td.text.strip()
                        if td_text not in ("雄性","雌性"):
                            if td_text.find("[") != -1:
                                td_text = td_text[:td_text.find("[")]
                                
                            if td_text.find("迷你：") != -1 and td_text.find("標準") != -1:
                                lindex = td_text.find("迷你：")+3
                                rindex = td_text.find("標準")
                                td_text[lindex:rindex]
                                td_text = td_text[lindex:rindex]
                    
                else:
                    continue
                dog_dict[th_text] = td_text
        time.sleep(0.5)
        return dog_dict
        
    except IndexError:
        print("沒有表格資料")

#6.建立類別彙整來自 CSV檔(List) 跟 爬取子頁面的資料(Dictionary)的資料
class DogBasic(object):
    title="狗的基本資料"
    def __init__(self,dog_list):
        self.eng_name=dog_list[0]
        self.chi_name=dog_list[1]
        self.type = dog_list[2]
        self.origin =dog_list[3]
        self.__src = dog_list[4]
        
    def getImg(self):
       return self.__src
        
#繼承自Dog_basic 建立類別Dog，傳入兩個參數(陣列和字典)
class Dog(DogBasic):
    table = {'別名': 'nickname', '體重': 'weight', '身高': 'height', '壽命': 'life'}
    def __init__(self,dog_list, dog_dict):
        self.nickname="None"
        self.life="None"
        super().__init__(dog_list)
        #將抓去下來的{'別名':'拉布拉多'} 由上面的table轉成nickname 接著設定self.nickname = "拉布拉多"
        try:
            for key_chi, value in dog_dict.items():
                key_eng = self.table.get(key_chi)
                setattr(self, key_eng, value)  #由於抓下來的資料不一定(別名體重身高壽命)每個都有，所以使用setattr動態設定
        except:
            print("Key not exist Error")

#7.建立實體物件，並將物件放入陣列(List)中
# 函式query("阿拉斯加")會從CSV檔取得一陣列，List索引1為完整名字"阿拉斯加雪撬犬"，呼叫get_dog_info()函式進行爬蟲取得一字典資料， 將陣列跟字典傳入Dog則可以建立一物件
dog_obj_list = []
print("爬蟲中，請稍等3秒")
for dog_list in [ query("雪納瑞"), query("拉布拉多"), query("阿拉斯加"),query("馬爾濟斯"),query("伯恩山犬"),query("米格魯") ]:
    dogname = dog_list[1]
    dog_dict = get_dog_info(dogname)
    dog_obj = Dog(dog_list, dog_dict)
    dog_obj_list.append(dog_obj)

#8.將物件的屬性值取出，用"""長字串"""寫成HTML網頁標籤的格式
dog_divs =""

for dog_obj in dog_obj_list:
    dog_div  = f"""<div class='dog'>
                       <h3>{dog_obj.chi_name}</h3>
                       <img src='{dog_obj.getImg()}' title='{dog_obj.chi_name}' 
                            onclick="bark(this.title)" onmouseover="clickable(this)" />
                       <p>別名: {dog_obj.nickname}</p>
                       <p>英文名: {dog_obj.eng_name}</p>
                       <p>原產國: {dog_obj.origin}</p> 
                       <p>種類: {dog_obj.type}</p> 
                       <p>體重: {dog_obj.weight}</p> 
                       <p>身高: {dog_obj.height}</p> 
                       <p>壽命: {dog_obj.life}</p> 
                   </div>"""
    dog_divs += dog_div
    
style = """#flex-container {
        width: 55vw;
        display: flex;
        flex-wrap: wrap;
        margin: 0 auto;
        padding: 10px;
      }
      h3,p {
        padding-left: 30px;
      }
      img {
        width: 220px;
        height: 220px;
        border-radius: 0.5rem;
        display: block;
        margin: 0 auto;
      }
      img:hover {
        transform: scale(1.2);
      }
      .dog {
        margin: 12px auto;
        width: 280px;
        border: 2px solid dimgray;
      }
"""
script = """<script>
        function bark(name){
            alert("這是一隻"+name);
        }

        function clickable(obj){
            obj.style.cursor='pointer'
        }
    </script>"""
#9.傳入HTML標籤和CSS,JS語法的參數後輸出網頁檔案
with open("DogPage.html", "w", encoding='utf-8') as dogPage:
    dogPage.write(
f"""<!DOCTYPE html>
<html > 
  <head> 
  <meta charset="UTF-8">
  <title>Dog Web Page</title> 
    <style> 
    {style}
    </style> 
  </head> 
  <body> 
    <div id='flex-container'>
        {dog_divs}
    </div> 
        {script}
  </body> 
</html>"""
    )
    print("DogPage.html 建立成功")
          