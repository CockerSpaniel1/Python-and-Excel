'''
物件導向
提高軟重的重用性,靈活性,擴充性
透過物件,存取或修改相關物件所連結的資料

'''

#定義類別(藍圖),使用class 關鍵字
class ADS():
    #屬性,特色,變數
    no=1
    name=''
    price=0.0

    #建構子(函數,式)(Constructor)
    #若未建立建構子,則會使用預設的建構子
    # def __init__(self):
    #     print("welcome to new Kaohsiung ad union!!")

    def showInfo(self):
        print("廣告編號：",self.no)
        print("廣告名稱：",self.name)
        print("廣告價格：",self.price)


#建立一個實體物件變數
ads=ADS()
ads.showInfo()  #『.』,Invoke method (調用方法)

print("\n----------------")
ads.no=2
ads.name="中元節買三送一"
ads.price=5000
ads.showInfo()

print("\n--自訂建構子(式)(constructor)---------------")
#自訂建構子(式)(constructor)
class AdsCategory():
    title="這是廣告類別"

    #建構子,設定建立物件時的初值
    def __init__(self,id,category):
        self.id=id
        self.category=category
        

    def showInfo(self):
        print(self.title)
        print("類別編號：",self.id)
        print("類別名稱：",self.category)


ac=AdsCategory('c01','TV')
ac.showInfo()

ac.category='YouTube'
ac.showInfo()



#建立顧客管理系統之顧客的藍圖
class Customer():

    #建構子
    def __init__(self,no,name,gender,email,tel,money):
        self.no=no
        self.name=name
        self.gender=gender
        self.email=email
        self.tel=tel
        self.money=money

    def cusInfo(self):
        print("客戶編號：",self.no)
        print("客戶姓名：",self.name)
        print("客戶性別：",self.gender)
        print("客戶電郵：",self.email)
        print("客戶電話：",self.tel)
        print("訂購金額：",self.money)
        

print("\n-NEW AD  Customer 管理系統-----------------------------")
husky=Customer('H01','艾呆丸','男','taiwan@gmail.com','07-1234567',2000000)
husky.cusInfo()
print("\n----after----------")
husky.gender="不願透露"   
husky.cusInfo()     

