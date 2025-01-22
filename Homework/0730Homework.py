menu = {'經典披薩': 329, '紐約披薩': 239, '瑪格麗特披薩': 289, '夏威夷披薩': 309, '海鮮披薩': 399}
order = {}

i=1
for pizza in menu:
    price = menu.get(pizza)
    print("-"*25)
    print(f"| {i}. {pizza:<{12-len(pizza)}}  ${menu.get(pizza)} |")
    i+=1
print("-"*25,"\n")

flag = True
while flag:
    option = int(input('1.經典披薩 2.紐約披薩. 3.瑪格麗特披薩 4.夏威夷披薩 5.海鮮披薩 6.結帳: \n輸入1~6 ==> ') )
    
    if option==6:
        j = 1
        total = 0
        for pizza in order:
            detail = order.get(pizza)       
            total += detail["subtotal"]
            print(f'商品{j}: {pizza:<{12-len(pizza)}}  價格: {detail["price"]}  數量: {detail["qty"]} 小計: {detail["subtotal"]:>4d}')
            j += 1 
        print(f"商品總金額: ${total}")
        flag=False

    elif option in list(range(1,6)):
        pizza = list(menu.keys())[option - 1]
        price = menu.get(pizza)
        qty = input(f"{pizza} ${price} \n請輸入訂購數量 ==> ")
        subtotal = price * int(qty)

        order[pizza] = {"price": price, "qty": qty, "subtotal": subtotal}




