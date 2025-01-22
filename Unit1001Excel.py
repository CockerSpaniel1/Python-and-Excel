import pandas as pd
 #pip install openpyxl
 #https://www.python-excel.org/

fin=pd.read_excel('https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx')

print(fin)

print('\n----fin col----------')
fin_col=pd.read_excel('https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx',usecols="A:C,E,G,H,K,M")

print(fin_col)

print('\n----fin row----------')
fin_row=pd.read_excel('https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx',usecols="A:C,E,G,H,K,M",nrows=8)

print(fin_row)

print('\n-------fin row2----------')
fin_row2=fin_col[0:10]
print(fin_row2)

print('\n-------fin part-----------')
fin_part=fin.at[5,'Country']
print(fin_part)