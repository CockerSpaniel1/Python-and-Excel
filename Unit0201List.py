#List 容器
#串列, 清單或列表
#其他語言,Array(陣列)
#串列的資料,稱元素
#每個元以『,』隔開

#宣告容器
fruit=["Apple","Banana","Cherry","Durian","Egg Fruit"]
print(fruit)
print(fruit[0]) #索引值由0開始
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])


#走訪list 元素(element)
print("\n-------for-----------------")
for e in fruit:
    print(e)

#查看型別
print(type(fruit))  #<class 'list'>

season=["Q1","Q2","Q3","Q4"]
print("\n-------season-----------------")
for e in season:
    print(e)

budget=[25,20,30,15]
total=0
print("\n---預算-------------")
for e in budget:
    total +=e
    print(e)

print("年度總預算",total," 萬元整")

print("\n---預算2-------------")
total=0
for i in range(0,len(season)):
    total +=budget[i]
    print(season[i],"--->",budget[i])

print("年度總預算2",total," 萬元整")

print("一年有",len(season),"季")    # len()求List 之長度