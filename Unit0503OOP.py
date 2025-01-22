import math
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #禸建保留方法,加法,減法,乘法,除法..的運算子重載
    def __add__(self,other):
        return Vector(self.x + other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x - other.x,self.y-other.y)
    
    def __str__(self):
        return f"Vector({self.x,self.y})"
    

#建立Vector 實體
v1=Vector(5,10)
v2=Vector(50,100)

#加法運算
v3=v1+v2
print(v3)

#減法運算
v4=v2-v1
print(v4)

        
        