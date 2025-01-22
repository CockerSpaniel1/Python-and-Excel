'''
Set 集合
無順序,
無重複
和dict 類似
一組key 集合,不儲存value
key 不能重複

'''

fruit={"Apple","Banana","Cherry","Durian","Egg Fruit"}
print(fruit)
print(type(fruit))

#走訪set
print("\n-------走訪set-----------------")
for e in fruit:
    print(e)

print("共有",len(fruit), "個元素")

fruit.add("Mango")
print("增加了mango 後, 共有",len(fruit), "個元素") #6

fruit.add("Cherry")
print("增加了Cherry 後, 共有",len(fruit), "個元素") #6

fruit.remove('Cherry')
print("移除了Cherry 後, 共有",len(fruit), "個元素") #5

fruit.update('Mango') #將Mango 每一個字母轉為元素
print(fruit)
print("共有",len(fruit), "個元素")


#fruit.remove('Cherry') KeyError: 'Cherry'
fruit.discard('Cherry') #元素不存在,不會發生error