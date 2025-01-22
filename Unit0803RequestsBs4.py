import requests
import bs4

url="https://www.python.org/"
page=requests.get(url)
page.encoding='utf-8'



#soup=bs4.BeautifulSoup(page.text,'lxml')   #第三方解析器
soup=bs4.BeautifulSoup(page.text,'html5lib')

print('\------擷取 link----------')
link_soup=soup.select('link')
print(type(link_soup))#<class 'bs4.element.ResultSet'>
print(link_soup)
print('共有<link> element',len(link_soup) )


print('\------擷取 button----------')
btn_soup=soup.select('button')
print(type(btn_soup))#<class 'bs4.element.ResultSet'>
print(btn_soup)
print('共有<button> element',len(btn_soup) )

print('\------擷取 img----------')
img_soup=soup.select('img')
print(type(img_soup))#<class 'bs4.element.ResultSet'>
print(img_soup)
print('共有<img> element',len(img_soup) )

for e in img_soup:
    print(e.get('src'))