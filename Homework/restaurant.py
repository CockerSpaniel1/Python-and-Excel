import time as t

#印出菜單
def print_menu(menu):
    i=1
    for pizza in menu:
        price = menu.get(pizza)
        print("-"*28)
        print(f'| {i}. {pizza:<{12-len(pizza)}}  ${menu.get(pizza)} 元 |')
        i+=1
    print("-"*28,"\n")

#點餐
def order_pizza(menu, option, discount=False):
    pizza = list(menu.keys())[option - 1]
    price = menu.get(pizza)
    if discount:
        qty = 1
    else:
        qty = int(input(f'{pizza} ${price} \n請輸入訂購數量 ==> '))
        if qty==0: qty=1
    subtotal = price * qty

    return pizza, {"price": price, "qty": qty, "subtotal": subtotal}

#取得當前時間的字串
def order_time():
    now = t.localtime(t.time())
    str_now = t.strftime('%Y/%m/%d %H:%M:%S',now)
    return str_now

#結帳
def check_out(order, discount=False):
    j = 1
    total = 0
    for pizza in order:
        detail = order.get(pizza)       
        total += detail["subtotal"]
        print("-"*54)
        print(f'|商品{j}: {pizza:<{12-len(pizza)}}  價格: {detail["price"]}  數量: {detail["qty"]}  小計:{detail["subtotal"]:>4d}元|')    
        j += 1 

    if discount: total=799
    print("-"*54)
    print(f'|商品總金額: {"$":>34s}{total:>4d}元|')
    print("-"*54)
    print(f'|結帳時間: {order_time():>42s}|')
    print("-"*54)
