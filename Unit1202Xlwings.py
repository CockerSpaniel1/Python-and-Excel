'''
資料轉換
'''

import pandas as pd
import xlwings as xw
import datetime as dt

wb=xw.Book('NetworkTraffic.xlsx')
sht=wb.sheets['資料集1']
sht.select() 

print('-------維度------')
print("B2 Cell Value :", sht.range('B2').value)

print('------強調-1 維度------')
print("B2 Cell Value ,1D:", sht.range('B2').options(ndim=1).value)


print('------強調-2 維度------')
print("B2 Cell Value ,2D:", sht.range('B2').options(ndim=2).value)

print('------強調-2 範圍 維度------')
print("B2 Cell Value ,2D:", sht.range('B2:D11').options(ndim=2).value)

print('\n------數值-int-----')
print("B2 Cell Value ,int :", sht.range('B2').options(numbers=int).value)

print('\n----日期-------')
sht2=wb.sheets.add("MyDate",after=2)

sht2.range('A1').value='2024/8/29'
print('預設日期格式：',sht2.range('A1').options(dates=dt.date).value)

#Lambda 匿名函稱
#java, C#, python 都有支援
#不需要函數名稱,只要一行運算式
date_handler=lambda year,month,day, **kwargs: "%04d年%02d月%02d日" %(year,month,day)
d=sht2.range('A1').options(dates=date_handler).value
print('自訂日期格式：',d)

