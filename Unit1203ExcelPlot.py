import matplotlib.pyplot as plt
import xlwings as xw


wb=xw.Book('NetworkTraffic.xlsx')
wb_count=wb.sheets.count    #工作表數量


try:
    wb.sheets.add('廣告',after=wb_count)
except:
    print('廣告工作表已存在')

sht=wb.sheets['廣告']

fig=plt.figure()
plt.plot(['google','yt','fb','ig'],[20,10,30,15])

sht.pictures.add(fig,name='myads',update=True)