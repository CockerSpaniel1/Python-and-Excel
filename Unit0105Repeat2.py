#重複流程控制
print("-------while, 1 加 100-----------------")
i=1
sum=0 
while i<=100:
    sum +=i #sum=sum+i
    #print("i=",i,"sum=",sum)
    print("i=%3d,sum=%4d"%(i,sum))
    i +=1

print("-------while, 1 加 100--之偶數相加---------------")
i=2
sum=0 
while i<=100:
    sum +=i #sum=sum+i  
    print("i=%3d,sum=%4d"%(i,sum))
    i +=2

print("\n-------break-----------------------")
i=1
sum=0 
while i<=100:
    if i==50:
        break   #跳離迴圈,不再回來
    sum +=i #sum=sum+i   
    print("i=%3d,sum=%4d"%(i,sum))
    i +=1

print("--continue-----while, 1 加 100--之偶數相加---------------")
i=1
sum=0 
while i<=100:
    i +=1
    if i % 2==1:    #%求餘數
        continue    #跳離迴圈,下一圈再回來
    sum +=i #sum=sum+i  
    print("i=%3d,sum=%4d"%(i,sum))
   
print("\n-----for---range(end)----------------------")
for i in range(10): #0~9
    print(i)

print("\n-----for---range(start,end)----------------------")
for i in range(1,10): #0~9
    print(i)

print("\n-----for---range(起,訖,等差值)----------------------")
for i in range(0,10,3): #0~9
    print(i)

print("\n-----for---range(起,訖,等差值)-----else-----------------")
for i in range(0,10,3): #0~9
    print(i)
else:
    print("~~~~~已經完成囉!!~~~~~~~~~")



print("\n---------nest loop------------")
k=0 #記錄乘積
for i in range(1,10):    #outer
    for j in range(1,10):    #inner
        k=i*j
        print("%d X %d = %2d"%(i,j,k),end="  ")
    print()
        