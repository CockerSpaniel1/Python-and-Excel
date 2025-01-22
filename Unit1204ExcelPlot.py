import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

import xlwings as xw

#處理中文亂碼
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']

#讀取Excel 工作表的資料
#python 繪製統計圖表
#放在Excel 工作表內
wb=xw.Book('NetworkTraffic.xlsx')
sht=wb.sheets['資料集1']
country=sht.range("A2:A11").options(ndim=1).value #y軸
user=['user','new user'] #x 軸
data=np.array(sht.range("B2:C11").options(ndim=2,numbers=int).value)    #資料來源

print(country)
print(user)
print(data)


fig, ax = plt.subplots()
im = ax.imshow(data,cmap='Spectral')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(user)), labels=user)
ax.set_yticks(np.arange(len(country)), labels=country)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(country)):
    for j in range(len(user)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

ax.set_title("各個國家GA 流量分析")
fig.tight_layout()
#plt.show()

sht.pictures.add(fig,name='ga',update=True,left=800,top=0)
wb.save()
wb.close()