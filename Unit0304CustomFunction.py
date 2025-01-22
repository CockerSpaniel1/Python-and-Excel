#*args 沒有限定參數的長度
#**kwargs 必須有變數名稱之參數(關鍵字參數),包成字典資料型態,使用** 符號

def myFruit(*args):
    print("\n--myFruit()---------------")
    print(type(args))   #Tuple
    return args

def yourFruit(**kwargs):
    print("\n--yourFruit()----------------")
    print(type(kwargs)) #dict
    return kwargs

print(myFruit("Apple","Banana","Cherry"))
print(yourFruit(origin='旗山',name='香蕉',price=50))

#-------------------------
#接受另一個函數作參數,無限定長度的參數,要有變數名稱之參數,將*args,**kwargs來將其他參數傳遞給這函數
def cafe(func,*args,**kwargs):
    print("\n--cafe()-------------")
    print(func(*args,**kwargs))

def myCafe(*args):
    print("--myCafe()----------------")
    return args

cafe(myCafe,'Americano','Latte','Espresso')

#-------------------------------------------------
def yourCafe(**kwargs):
    print("--yourCafe()----")
    return kwargs

cafe(yourCafe,coffee='Latte',milk='Yes',sugar='No') #dict
cafe(yourCafe,american=55,latte=65,espresso=125)


def hisCafe(*args,**kwargs):
    print("--hisCafe()----")
    return args,kwargs

cafe(hisCafe,'Americano','Latte','Espresso',americano=55,latte=65,espresso=125) 