import matplotlib.pyplot as plt

#10 個數值元素list
mydata=[15,20,80,40,50,70,10,20,95,55]

'''

#預設 格式 藍色折線 'b-'
plt.plot(mydata)
plt.show()

#折線
plt.plot(mydata,'b-')
plt.show()

#綠圓形
plt.plot(mydata,'go')
plt.show()


#紅圓折形
plt.plot(mydata,'r-o')
plt.show()



#黃虛線形
plt.plot(mydata,'y--')
plt.show()



plt.plot(mydata,'b--s')
plt.axis((0,10,0,100))
plt.title('Advertising Budget',fontsize=16)
plt.show()


plt.plot(mydata,'k-^')
plt.axis((0,10,0,100))
plt.title('Advertising Budget',fontsize=16)
plt.show()
'''

plt.plot(mydata,linewidth=3,color='tomato')
plt.axis((0,10,0,100))
plt.title('Advertising Budget',fontsize=16)
plt.xlabel('month',fontsize=12,color='green')
plt.ylabel('budget',fontsize=12,color='green')
plt.tick_params(axis='both',labelsize=10,color='red')
plt.show()