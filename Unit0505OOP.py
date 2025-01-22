#Encapsulation,封裝
#資料和方法包裝在一起,限制外面對它們的直接存取
#通常會使用私有(private)屬性來呈現

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance  #私有屬性
    

    def deposite(self,amount):
        if amount>0:
            self.__balance +=amount

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance -=amount

    def getBalance(self):
        return self.__balance
    

account=BankAccount(1000)
account.deposite(500)
account.withdraw(300)
print(account.getBalance())
#print(account.__balance) #AttributeError