import json
import os
import time as t
import random as r

class Customer:
    def __init__(self, name, email, tel, order_obj):  
        self.name = name
        self.email = email
        self.tel = tel
        # 用另一個物件當屬性值(在class裡放另一個class)
        self.order_obj = order_obj
        print(f'(Customer的物件初始化) 訂購者: {self.name}, 訂單編號: {self.order_obj.id}, 訂購時間: {self.order_obj.time}, \n訂單內容: {self.order_obj.pizza}')
        print('----------------------------------------------')

    def write_json(self):
        # 寫成單份json
        cust_dict = {
            "客戶姓名": self.name,
            "客戶電郵": self.email,
            "客戶電話": self.tel,
            "訂購時間": self.order_obj.time,
            "訂單編號": str(self.order_obj.id),
            "訂單內容": self.order_obj.pizza,
        }

        with open(f".\\Document\\{self.name}.json", "w", encoding="utf-8") as wf:
            json.dump(cust_dict, wf, indent=4, ensure_ascii=False)

class Order:
    count = 1

    def __init__(self, pizza):
        self.pizza = pizza
        self.id = Order.count
        Order.count += 1
        self.time = self.order_time()

        print(f'(Order的物件初始化) 訂單{self.id } 建立成功')


    def order_time(self):
        now = t.localtime(t.time() + 600 * r.randint(1, 18))
        str_now = t.strftime("%Y/%m/%d %H:%M:%S", now)
        return str_now


folder = "Document"
try:
    os.mkdir(folder)
except FileExistsError:
    print(f"資料夾: {folder} 已存在")
else:
    print(f"資料夾: {folder} 建立成功")
finally:
    print(f"------------Finally的分隔線------------------------")


husky = Customer(name="哈士奇", email="husky@gmail.com", tel="0987654321",
                    order_obj=Order( pizza={"經典披薩": 1, "紐約披薩": 1, "瑪格麗特披薩": 1} ) )

chihuahua = Customer(name="吉娃娃", email="chihuahua@hotmail.com", tel="0912345678",
                        order_obj=Order( pizza={"瑪格麗特披薩": 1, "夏威夷披薩": 1, "海鮮披薩": 1} ) )


pizza = Order(pizza={"瑪格麗特披薩": 3})
schnauzer = Customer(name="雪納瑞",email="schnauzer@yahoo.com", tel="0911223344",
               order_obj = pizza)



husky.write_json()
chihuahua.write_json()
schnauzer.write_json()

