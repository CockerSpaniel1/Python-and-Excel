'''
requests package(套件)
'''

import requests #要先安裝 pip install requests

url='https://www.python.org'
page=requests.get(url)

print(page) #<Response [200]>,請求已成功,ok,200

page.encoding='utf-8'
print(type(page))   #<class 'requests.models.Response'>

print("\n--------------------------------------------s")
#print(page.text)

#if page.status_code==requests.codes.ok:
if page.status_code==200:
    #print(page.text)
    print("page.text 的長度：",len(page.text))
    try:
        wf=open('pythonpage.txt','w',encoding='utf-8')
        wf.write(page.text)
        print("write successed!!")
    except:
        print("write failed!!")
    finally:
        print("~~~~~~~the end~~~~~~~~~~~")
        wf.close()
else:
    print('capture failed!!')