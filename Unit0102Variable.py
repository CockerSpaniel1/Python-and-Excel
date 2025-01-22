#宣告變數
fruit="芒果"    #fruit 為變數名稱,"芒果"是變數的值, = (指定或指派運算子), 將"芒果"指定給fruit 變數
price=150
breed="愛文"

#單一值,指定給多個變數
price2=price3=price4=100

#同一行,指定多個變數的值
fruit5,price5,breed5="香蕉",69.9,"旗山"


fruit6="cherry"

#輸出
print("水果特價：",fruit)
print("水果售價：",price)
print("水果品種：",breed)

#輸出,單一值,指定給多個變數
print("price2=",price2)
print("price3=",price3)
print("price4=",price4)

#輸出,同一行,指定多個變數的值
print("fruit5=",fruit5)
print("price5=",price5)
print("breed5=",breed5)

price5=price5+5
print("price5漲價後為",price5) #74.9

print("水果名稱:",fruit6)

#刪除變數
del fruit6
#print("水果名稱:",fruit6) #error ,因為fruit6已被刪除


