#靜態方法(static method)
#使用@staticmethod 修飾器

class MyClass(object):

    @staticmethod
    def addFun(x,y):
        return x+y
    

print(MyClass.addFun(5,10))


