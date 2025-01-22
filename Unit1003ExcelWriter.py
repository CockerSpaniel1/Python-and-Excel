'''
pandas.ExcelWriter
將DataFrame 物件寫入到Excel 工作表的類別

engine xlsx 使用openpyxl
https://www.python-excel.org/
'''

import pandas as pd

order_col=['order_no','p_name','catagory','supplier','qty','price']
order_row=[
    ['20240827001','Apple','Fruit','North com',5,100.0],
    ['20240827001','Banana','Fruit','North com',6,90.0],
    ['20240827001','Cherry','Fruit','East com',8,150.0],
    ['20240827001','高麗菜','Vegetable','South com',50,50.0],
    ['20240827001','花椰菜','Fruit','Center com',10,55.0],
]

print('\n-----建立Excel 檔案和工作表---------')
order=pd.DataFrame(order_row,columns=order_col)
file='OrderDetail.xlsx'
sheet='order'

with pd.ExcelWriter(file) as writer:
    order.to_excel(writer,sheet_name=sheet)
    print('%s 檔案已經建立'%file)
    print('%s 工作表已經建立'% sheet)


#-------------------------------------------------------------
order_col=['p_name','price','cost']
order_row=[
    ['Apple',100.0,50.0],
    ['Banana',90.0,45.0],
    ['Cherry',150.0,75.0],
    ['高麗菜',50.0,25.0],
    ['花椰菜',55.0,20.0],
]
order=pd.DataFrame(order_row,columns=order_col)
file='OrderDetail.xlsx'
sheet='prducts'

with pd.ExcelWriter(file,mode='a',engine='openpyxl') as writer:
    order.to_excel(writer,sheet_name=sheet)
    print('%s 檔案已經建立'%file)
    print('%s 工作表已經建立'% sheet)
