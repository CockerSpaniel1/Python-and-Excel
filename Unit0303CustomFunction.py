#四種自訂函數的狀態

# 1. 無參數(parameter),無傳回值(return)
def myfun():
    print("\n------本年度廣告預算審查中---------------")

# 2. 有參數(parameter),無傳回值(return)
def yourfun(ads):
    print("今年的廣告主要平台為：",ads)

# 3. 無參數(parameter),有傳回值(return) 
def hisfun():
    return "廣告儘快審核中...."

# 4. 有參數(parameter),有傳回值(return) 
def herfun(budget):
    return "廣告預算:" + str(budget) + " 萬元 "     #若沒有使用str()轉型,則會發生error

#自訂函數的實例應用
#身體質量指數bmi
#print(pow(10,2)) #求幾次方的內建函數
def bmi(h,w):
    b=round(w/pow(h/100,2),1)
    return b

#有預設值的參數
def ourfun(budget=50):
    return "廣告預算:" + str(budget) + " 萬元 "

#多個傳回值
def multi_return(m,n):
    add=m+n
    sub=m-n
    pro=m*n
    div=m/n
    return add,sub,pro,div

#函數作為參數
def fruit(p):
    return p.lower()    #轉為小寫

def favorite(f):
    s=''
    if f=='a':
        s='Apple'
    elif f=='b':
        s="BANANA"
    elif f=='c':
        s="cHErry"
    else:
        s='Sorry, I do\'nt know what this is'
    return s

    

#呼叫自訂函數
myfun()
yourfun("Youtuber")
print(hisfun())
myads=hisfun()
print(myads)
print(herfun(100))


mybmi=bmi(175,65)
print("紅人的BMI:", mybmi)

print(ourfun()) #因為有預設值,所以若無給予引數,不會生error
print(ourfun(200))  


print(multi_return(5,2))
print(type(multi_return(5,2)))  #<class 'tuple'>

print(favorite(fruit('b')))
print(favorite(fruit('A')))