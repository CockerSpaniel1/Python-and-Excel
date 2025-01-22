price,price2=100,200

print("Mango Price:",price)
print("Banana Price:",price2)


#條件式流程控制,單一條件,單一敘述
if price<price2:
    print("Banana 比較貴")
    
if price>price2:
    print("Mango 比較貴")


#單一條件,多重敘述
print("\n---------------------------")
if price<price2:
    print("Banana 比較貴")
else:
    print("Mango 比較貴")


print("\n---------------------------")
cp=int(input("請輸入櫻桃的價格:"))


#多個條件
if cp<100:
    print("趕快去搶購")
elif cp==100:
    print("讓我想想")
else:
    print("太貴了,呷不起")

print("\n------int()-------")
num=999.9
print("num",num)
print("num",int(num))

