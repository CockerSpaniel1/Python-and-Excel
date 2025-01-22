'''
例外處理
Exception
'''

import os
import sys

i=10
print(f'i={i}')

#j=10
#print(f'j={j}') #NameError: name 'j' is not defined

#print("hello") #若前述發生Error, 此行不會執行


#Exception 區塊
try:
    print(f'j={j}')
except:
    print('Variable is not defined!!')
    print("***********", sys.exc_info())

print("hello")  #若前述發Exception ,此行會執行

folder='myad'
yourfolder='yourad'

#os.mkdir(folder)

#單一except
print('\n--單一except-------------')
try:
    os.rmdir(folder)
    print(f'{folder} deleted!!')
except:
    print(f'{folder} No Such folder!!')


print("hello2")


#多重except
print('\n--多重except-------------')
try:
    os.rmdir(folder)
    print(f'{folder} deleted!!')

    os.mkdir(yourfolder)
    print(f'{yourfolder} crteated!!')

    print("var=",var)    #變數沒有宣告
except FileNotFoundError:
    print(f'{folder} No such folder!!')
except FileExistsError:
    print(f'{yourfolder} already exists!!')
except NameError:
    print("Variable not defined!!")
except:
    print('Other Error')
    print('please Call MIS, TEL:07-1234567#123')


#沒有發生error ,才執行
slogan="Enjoy the science and Technology"

print("\n--else------------")
try:
    print(slogan)
except:
    print("不知所云!!")
else:
    print("恭喜你,沒有發生錯誤")    #沒有發生error時，才執行


#不論是否error, 皆會執行
print("\n--finally------------")
try:
    print(slogan)
except:
    print("不知所云!!")
finally:
    print("---the end--------")


print("\n--try...except...else....finally------------")
try:
    print(slogan)
except:
    print("不知所云!!")
else:
    print("congratulations!!")  #沒有發生error, 才會執行
finally:
    print("---the end--------") #不論是否error, 皆會執行