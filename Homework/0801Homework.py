#需使用Terminal執行(Code Runner的Run Python Code)
#若使用預設(Run Code)執行，結果會印在OUTPUT欄，但無法輸入資料
import restaurant as rest
import random as r

menu = {'經典披薩': 329, '紐約披薩': 239, '瑪格麗特披薩': 289, '夏威夷披薩': 309, '海鮮披薩': 399}
order_form = {}

rest.print_menu(menu)

input_text = '點餐 1.經典披薩 2.紐約披薩. 3.瑪格麗特披薩 4.夏威夷披薩 5.海鮮披薩 6.三個披薩799(隨機口味) \n輸入1~6 ==> '
flag = True
fool_proofing = True

while flag:
    option = int(input(input_text))

    if option in range(1,6):
        pizza, detial = rest.order_pizza(menu, option) 
        order_form[pizza] = detial 

        next_option = int(input('1.繼續選購 2.結帳: \n輸入1~2 ==> ') )

        if next_option==2:
            rest.check_out(order_form)
            flag=False

        input_text = '點餐 1.經典披薩 2.紐約披薩. 3.瑪格麗特披薩 4.夏威夷披薩 5.海鮮披薩 \n輸入1~5 ==> '
        fool_proofing = False

    # 三個披薩799(隨機口味)
    elif option == 6 and fool_proofing:
        flavors = r.sample([1, 2, 3, 4, 5], k=3)

        for f in flavors:
            pizza, detial = rest.order_pizza(menu, f, discount=True) 
            order_form[pizza] = detial 

        rest.check_out(order_form, discount=True)
        flag=False
        
    else:
        print("請輸入數字1~6!")
    
        






