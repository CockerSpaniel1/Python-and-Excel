import pandas as pd
import dataframe_image as dfi   #匯出圖像

iTaiwan=pd.read_csv('https://data.kcg.gov.tw/dataset/cb853667-22aa-41c0-a0d1-8f246fa124df/resource/7c925857-2778-4b66-b926-b5e25c913c42/download/111itaiwanhotspots.csv')


#print(iTaiwan)
print(iTaiwan.head())

#轉為圖像
#若記錄超過100筆,則會發生error,故要使用max_rows 限制筆數大小
dfi.export(iTaiwan,'iTaiwan.png',max_rows=100)

#建立HTML file
file=open('iTaiwan.html','w',encoding='utf-8')
iTaiwan_html=iTaiwan.to_html()
file.close()

print('\n---------資料型態----------------')
print(type(iTaiwan))    #<class 'pandas.core.frame.DataFrame'>
print("筆數：",len(iTaiwan))#315

print("\n--------欄名---------------")
print(iTaiwan.columns) #Index(['地點', '地址', 'latitude', 'longitude'], dtype='object')

print(iTaiwan.index)

print("\n----------第0筆---------------")
print(iTaiwan.head(1))

print("\n----------從後方輸出筆數---------------")
print(iTaiwan.tail(5))

print("\n----------說明或描述---------------")
print(iTaiwan.describe())

print('\n------分別顯示欄位名稱------------------')
print(iTaiwan.columns[0]) 
print(iTaiwan.columns[1])
print(iTaiwan.columns[2])
print(iTaiwan.columns[3])