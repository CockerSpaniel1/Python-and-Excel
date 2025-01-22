#繼承
#上類別(super class)
class Animal(object):   #所有的類別都繼承object,可省略
    title="I am Animal"
    def __init__(self,category,live) :
        self.category=category
        self.live=live
        
    #setter
    def setCategory(self,category):
        self.category=category

    def setLive(self,live):
        self.live=live

    def setAll(self,category,live):
        self.category=category
        self.live=live

    #getter
    def getCategory(self):
        return self.category
    
    def getLive(self):
        return self.live
    
    def getAll(self):
        return self.category,self.live


#衍生類別(derived class)
class Bird(Animal):
    def __init__(self):
       self.__title="我是一隻鳥"
       self.__fly="我會飛高高"

    def getInfo(self):
        return self.__title,self.__fly

class Orstrich(Bird):
    def __init__(self):
        self.__title="我是一隻鴕鳥"
        self.__fly="我不會飛,但我會把頭埋到土裡"
        super().__init__()  #調用上類別的建構子

    def showInfo(self):
        print(self.__title)
        print(self.__fly)
        print(super().getInfo())    #調用上類別的方法
        super().setCategory('禽類')
        print(super().getCategory())


class Fish(Animal):
    def __init__(self):
        self.__title="我是一隻魚"
        self.__swimming="我會在水裡游" 


#-------------------------------------------------------
#建立實體
ani=Animal('貓科','陸地')
print(ani.getCategory())
print(ani.getLive())
print(ani.getAll())


ani.setCategory('犬科')
print(ani.getCategory())

print("\n-----Brid----------")
bird=Bird()
print(bird.getInfo())

print("\n-----Ostrich---------------")
ostrich=Orstrich()
ostrich.showInfo()

print("\n------------------------")
print(ani.category)
#print(ostrich.__fly) #無法讀取

print("\n--------------------")
print(type(ostrich))   #<class '__main__.Orstrich'>
print(isinstance(ostrich,Animal)) #True
print(isinstance(ostrich,Bird)) #True
print(isinstance(ostrich,Orstrich)) #True
print(isinstance(ostrich,Fish)) # False
