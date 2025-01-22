#dict 字典,容器
#元素以『key(鍵)』,『value(值)』配對的方式儲存
#字串、整數、浮點數等可以為『鍵』
#以{} 括住
#key:value

fruit={
    "Apple":250,
    "Banana":99,
    "Chery":350,
    "Durian":450,
    "Egg Fruit":250
}

print(fruit)
print(type(fruit))

print("fruit所有的鍵：",fruit.keys())   #取得鍵,使用keys() 函數
print("Durian價格：",fruit.get("Durian"),"元")#取回鍵的值

print("\n-----------走訪dict--------------------")
for e in fruit:
    #print(e,"--->",fruit.get(e),"元")
    print("%-10s\t-->\t%3d元"%(e,fruit.get(e)))

cake={
    "鳯山":{
        "蓮蓉":1000,
        "桂圓":950,
        "綠豆踫":500,
        "水果":650
    },
    "新興":{
        "蓮蓉":1000,
        "桂圓":950,        
        "水果":650
    },
    "巨蛋":{
        "蓮蓉":1000,
        "桂圓":950,
        "綠豆踫":500       
    }
}

print("\n-----走訪dict----------")
for e in cake:
    for ee in cake.get(e):
        print("%-5s\t---->%-5s:\t%5d元"%(e,ee,cake.get(e).get(ee)))
    print()

#2D List (2維)
ads=[
    ['Q1',25],  
    ['Q2',20],  
    ['Q3',25],  
    ['Q4',30],  
]

#list 轉為dict
ads_dict=dict(ads)  #使用dict() 進行轉型
print(ads_dict)
print(type(ads_dict))

print("\n------直接使用dict()建立字典,methon 1-----------------------")
coffee=dict(美式=550,拿鐵=450,卡布=500)
print(coffee)
print(type(coffee))


print("\n------直接使用dict()建立字典,methon 2-----------------------")
bean=dict([
    ['阿拉比卡',800],
    ['藝伎',1200],
    ['耶加雪菲',850]
])

print(bean)
print(type(bean))

#鍵不可以重複(必須是唯一),值可以重複,若鍵重複,但後方會覆蓋前方的鍵
fruit_origin={
    1:"屏東",
    2:"高雄",
    3:"台南",
    2:"嘉義"
}

print(fruit_origin)