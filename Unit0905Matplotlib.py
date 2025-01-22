import matplotlib.pyplot as plt
import numpy as np


#處理中文亂碼
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']

qty=[55,65,50,75,90]
q_len=len(qty)
print("qty lenth:",q_len)

x_axis=np.arange(q_len)
print("x_axis:",x_axis)

width_bar=0.88
plt.bar(x_axis,qty,width_bar)
plt.xticks(x_axis,('美式','義式','拿鐵','卡布','藍山'))
plt.show()

coffee=plt.bar(x_axis,qty,width_bar,color='lightpink')
plt.title('咖啡銷售直條圖')
plt.xlabel('咖啡名稱')
plt.ylabel('數量')
plt.xticks(x_axis,('美式','義式','拿鐵','卡布','藍山'))
plt.yticks(np.arange(0,110,10))
plt.bar_label(coffee,padding=3)     # 標籤與bar 之間的距離
plt.show()