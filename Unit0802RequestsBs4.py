import requests,bs4,os

url="https://marketing-hsu01.web.app/fruit.html"
page=requests.get(url)
page.encoding='utf-8'
print(page)

#html.parser (python內建) ,解析器(剖析器) ,html,xml
soup=bs4.BeautifulSoup(page.text,'html.parser')
#print(soup)
#print(soup.prettify())  #如同字串,輸出到頁面元素

print("\n------------標題-----------------------------")
title_tag=soup.title
print("網站標題(html 標籤)：",title_tag)
print("網站標題：",title_tag.text)
print("網站標題：",title_tag.string)

print('\n----------格子----------------------')
td_tag=soup.find_all('td')
print(td_tag)

print("\n-----走訪list (格子)------------")
for tag in td_tag:
    print(tag.contents)


print('\n----------圖片----------------------')
img_tag=soup.find_all('img')
print("\n-----圖片,取得整個節點------------")
for tag in img_tag:
    print(tag)  #取得整個節點

print('\n----------圖片2---------------------')
img2_tag=soup.find_all('img')
print("\n-----圖片2,取得節點的屬性,圖片來源-------------")
for tag in img2_tag:
    print(tag.get('src'))  #取得節點的屬性,圖片來源

pos=url.rfind('/')  #從字串的右方開始搜尋
print(pos)  #31
web=url[0:pos+1] #取得索引位置0~32之間的字串
print(web)

print("\n---------圖片3,full src------------------")
img3_tag=soup.find_all('img')
for tag in img3_tag:
    src=tag.get('src')
    fullsrc=web+src
    print(fullsrc)
    file=src[src.rfind('/')+1:]
    print(file)

    if not os.path.exists('download_img'):
        os.mkdir('download_img')
    img=requests.get(fullsrc)   #下庫圖片檔
    with open("download_img\\" + file,'wb') as file: #開啟資料夾與圖片命名
        file.write(img.content) #寫入圖片以二進制位元碼