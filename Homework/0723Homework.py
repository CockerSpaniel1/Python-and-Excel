products= ["經典披薩", "紐約披薩", "瑪格麗特披薩", "夏威夷披薩", "海鮮披薩"]
prices = list((329, 239, 289, 309, 399))

for i in range(len(products)):
    print( f"{i+1}. {products[i]}  ${prices[i]}")


