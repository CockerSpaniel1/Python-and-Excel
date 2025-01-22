import numpy as np
import pandas as pd

arr=np.array([1,2,3])
print(arr)
print(type(arr))    #<class 'numpy.ndarray'>

arr2=np.arange(10)  #[0 1 2 3 4 5 6 7 8 9]
print(arr2)
print(type(arr2))   #<class 'numpy.ndarray'>,類似python 內建的range(),但傳回是array

arr3=np.linspace(0,8,5)
print(arr3)

#使用list ,建立series
n=pd.Series([2,4,6,8,np.nan,11])
print(n)


#使用np 亂數建series,自訂索引值
print('\n----------------------')
n2=pd.Series(np.random.random(6),index=['一','二','三','四','五','六'])
print(n2)
print(n2.index)

#使用dict 字典,建立series
fruit={'Apple':1,'Banana':2,'Cherry':3,'Durian':4}
n3=pd.Series(fruit)
#n3=pd.Series(fruit,index=['蘋果','香蕉','C','D'])
print(n3)
print(n3.index) #Index(['Apple', 'Banana', 'Cherry', 'Durian'], dtype='object')