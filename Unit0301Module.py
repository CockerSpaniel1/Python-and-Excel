#匯入內建模組
import sys
import platform as pf
import time as t
import random as r



print('----sys------------')
print('系統路徑')
print(sys.path)
print(type(sys.path))

print("----走訪sys.path----------")
for s in sys.path:
    print(s)

print("----platform----------")
print("作業系統",pf.system())
print("系統版本",pf.version())
print("python版本",pf.python_version())

print("----time----------")
print(t.time())

tt=t.localtime(t.time())
print(tt)
print(type(tt)) #<class 'time.struct_time'>

print("目前時間：%4d年%2d月%2d日 %2d:%2d:%2d "%(tt.tm_year,tt.tm_mon,tt.tm_mday,tt.tm_hour,tt.tm_min,tt.tm_sec))

print('\n---------random-----------------')
print("----------浮點數亂數------------")
for i in range(0,10):
    print(r.random(), end=" ")


print("\n---------整數亂數----------------")
for i in range(0,6):
    print(r.randint(1,49),end=" ")

print()
color="紅橙黃綠藍靛紫"
print(color)
for i in range(0,4):
    print(r.choice(color),end=" ")


print("\n------不重複 sample()-----------------------")
print(r.sample(color,7))
print(type(r.sample(color,7)))

print("\n------不重複 sample()-,大樂透----------------------")
print(r.sample(range(1,50),6))
