#Tuple 元組
#結構List 相同
#元素之值是不可修改
#是不可修改的List

#宣告元組
fruit=("Apple","Banana","Cherry","Durian","Egg Fruit")
print(fruit)
print(type(fruit))

#print(fruit(3)) #error

print(fruit[3])

#走訪tuple 元素(element)
print("\n-------for-----------------")
for e in fruit:
    print(e)

#fruit[3]="榴槤" #TypeError: 'tuple' object does not support item assignment

print("\n----------切片----------------")
print("fruit 第1,2個:",fruit[1:3])
print("fruit 第0,1,2個:",fruit[:3])
print("fruit 第3,4個:",fruit[3:])

print("\n-------tuple 轉為list-----------------")
fruit_list=list(fruit)  #使用list() 進行轉型
print("轉型後：",type(fruit_list))

print("\n-------list 轉為tuple-----------------")
fruit_tuple=tuple(fruit_list)   # tuple() 進行轉型
print("轉型後：",type(fruit_tuple))
