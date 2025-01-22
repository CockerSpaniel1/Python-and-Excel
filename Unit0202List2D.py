#2D List (2維)

ads=[
    ['Q1',25],  #ads[0][0],ads[0][1]
    ['Q2',20],  #ads[1][0],ads[1][1]
    ['Q3',25],  #ads[2][0],ads[2][1]
    ['Q4',30],  #ads[3][0],ads[3][1]
]

print(ads)
print(ads[1])
print(ads[1][0],ads[1][1])  #Q2,20

total=0 
print("\n----走訪二維list, method 1------------")
for e in ads:
    i=0
    for ee in e:
        if i==1:
            total +=ee
        print(ee, end="  ")
        i +=1
    print()

print("年度總預算：",total)

total=0 
print("\n----走訪二維list, method 2------------")
for i in range(len(ads)):
    for j in range(len(ads[i])):
        if j==1:
            total +=ads[i][j]
        print(ads[i][j],end=" ")
    print()

print("年度總預算：",total)

#修改list 元素的值
ads[2][1]=90
print("\nQ3修改後的預算為：",ads[2][1])

total=0 
print("\n----修改後的總預算------------")
for i in range(len(ads)):
    for j in range(len(ads[i])):
        if j==1:
            total +=ads[i][j]
        print(ads[i][j],end=" ")
    print()

print("年度總預算：",total)

