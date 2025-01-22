import pandas as pd

order=pd.DataFrame()
d=pd.read_excel('order.xlsx',sheet_name=None)
s=pd.ExcelFile('order.xlsx')

for name in s.sheet_names:
    order=pd.concat([order,d.get(name)])    #串接每張工作表的記錄
    #print(order)
    #print("\n-----------")


print(order)