import pandas as pd

#以series 或字典建立DataFrame

#建立字典dict
product={
    'coffee':pd.Series([1,2,3,4,5],index=["美式","義式","拿鐵","藍山","曼特"]),
    'bean':pd.Series([1,2,3],index=['肯亞','古巴','巴西'])
}

print('\n----output product dict---------------')  
print("product type:",type(product)) #<class 'dict'>
print(product)

#將字典轉為框架
cafe=pd.DataFrame(product)
print('\n----output cafe DataFrame---------------')  
print("cafe type:",type(cafe)) #<class 'pandas.core.frame.DataFrame'>
print(cafe)

#以list 字典為值,建立DataFrame
order={
    'name':['美式','義式','拿鐵','藍山','卡布'],
    'price':[95,105,125,150,130],
    'qty':[5,20,15,5,10]
}

order_df=pd.DataFrame(order)
print('\n-------output order_df DataFrame------------')
print(order_df)
