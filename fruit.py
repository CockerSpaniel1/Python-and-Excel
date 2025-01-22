#自訂函數
def favorite(name):
    print("您最喜愛的水果是:",name)

def sale(name,price):
    print("水果名稱：%s\n價格：%3d"%(name,price))

def onsale(name,cost,price,qty):
    gp=(price-cost)*qty #毛利
    print(f'水果名稱:{name},成本:{cost},價格:{price},數量:{qty},毛利:{gp}')

def dessert(*name): #可接收多個值
    print(name)
    print("資料型態",type(name))
    for e in name:
        print(e)

#處理傳入的值為dict 之函數
def detail(product):
    for e in product:
        print(e,":")
        item=product.get(e)
        for ee in item:
            print(ee,end="->")
            print(item.get(ee))
        print('---------------------------------')