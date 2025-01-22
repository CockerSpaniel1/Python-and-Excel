import matplotlib.pyplot as plt
import numpy as np

#處理中文亂碼
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']

fig, ax = plt.subplots()

size = 0.3  #radius
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20b"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])


#outer
labels_outer=['KAO1','KAO2','KAO2']
ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'),
       labels=labels_outer,
       labeldistance=1.05,
       autopct='%1.1f%%',
       pctdistance=0.85)


#inner
labels_inner=['飲品','豆子','飲品','豆子','飲品','豆子']
ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'),
       labels=labels_inner,
       labeldistance=0.35,
       autopct='%1.1f%%',
       pctdistance=0.8)


ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()