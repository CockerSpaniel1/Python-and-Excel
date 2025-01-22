'''
xlwings
透過python 程式來自動化excel
從Excel  調用 python
 xlwings

 https://www.xlwings.org/
 pip install xlwings

'''

import pandas as pd
import xlwings as xw

#建立活頁簿頁
#wb=xw.Book()   #建立新的EXcel 檔案
#wb=xw.Book('NetworkTraffic.xlsx')

#r'c:\Users\user\Documents\NetworkTraffic.xlsx',使用r 做為前綴, 告訴python 不要對字串中的反斜進行轉義
try:
    wb=xw.Book(r'c:\Users\user\Documents\NetworkTraffic.xlsx')
    sht=wb.sheets['資料集1']
    sht.select() #選擇資料集1工作表,作為作用中的工作表
    country=sht.range('A6').value
    print("國家：",country)

    #刪除某一範圍的內容
    sht.range("A12:J12").delete()

    #讀取某一範圍的內容
    print("\n---Read Range Data---------")
    print(sht.range('A1').expand().value)

    #讀取某一範圍的內容,轉為DF
    print("\n---------Read Range Data , DataFrame ----------")
    traffic=pd.DataFrame(sht.range('A1').expand().value)
    print(traffic)
    print(type(traffic))    #<class 'pandas.core.frame.DataFrame'>
except:
    print('Failed to open file worksheet!!')