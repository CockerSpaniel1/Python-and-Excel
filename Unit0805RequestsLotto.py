import requests

#發送GET 請求到API
url="https://api.taiwanlottery.com/TLCAPIWeB/Lottery/Lotto649Result?period&month=2024-08&pageNum=1&pageSize=50"

response=requests.get(url)

#檢查請求是否成功
if response.status_code==200:
    data=response.json()    #將回應的資料轉為json 格式

    #提取開獎的資料
    if 'content' in data and 'lotto649Res' in data['content']:
        results=data['content']['lotto649Res']  

        for index,result in enumerate(results): #將重複(迭代)內容的物件,像list ,tuple,string等,轉換為索引的序列
            draw_numbers=result.get('drawNumberSize',[])
            print(f'抽取2024年8月份各期的數字{index+1}:{draw_numbers}')
    else:
        print("不是JSON 的資料結構")
else:
    print(f'檢索資料失敗,狀態碼:{response.status_code}')
