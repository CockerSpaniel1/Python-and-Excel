'''
read | write CSV
'''

import csv

print('---read CSV file-----------------')

#cp950 (big5 ) 解碼中文字
#code page 950 ,微軟的繁中字元集標準,大五碼修改而成,目前最通行的版本

with open('.\\sample\products.csv','r',encoding='cp950') as rf:
    print(rf)
    print('\n------products.csv-------------')

    '''
    for e in csv.reader(rf):
        print(e)
    '''

    products=[k for k in csv.reader(rf)]
    print(products)

    print(type(products))

    print("\n---------------------")
    for e in products:
        print(e)
    print() 

    print("\n------write CSV file---------------------------")
    with open(".\\sample\products2.csv",'w',newline='') as wf:
        w=csv.writer(wf)
        w.writerows(products)
        print('write ok')


    