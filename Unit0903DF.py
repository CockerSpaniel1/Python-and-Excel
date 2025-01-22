import pandas as pd
import json

#高雄市預算
#budget=pd.read_json('https://api.kcg.gov.tw/api/service/get/3a3426ac-89cf-4e50-9828-349cb9296f6b')
budget=pd.read_json('kcg.json')
print('\n------output kcg budget-----------------')
print(budget)
print(type(budget)) #<class 'pandas.core.frame.DataFrame'>
print("col:",budget.columns)
print("index:",budget.index)


print("\n---------budget Data 欄位轉為DataFrame-----------------------------")
budget_data=pd.DataFrame(budget['data'])
print(budget_data) 




print("\n------DataFrame 轉為json---------------")
budget_json=budget_data.to_json()
print(budget_json)
print("type:",type(budget_json)) #<class 'str'>

print("\n------json- 轉為dict--------------")
budget_dict=json.loads(budget_json)
print("type:",type(budget_dict))    #<class 'dict'>
print(budget_dict)

print("\n------dict--轉為DataFrame------------")
budget_df=pd.DataFrame(budget_dict.get('data'))
print(budget_df)

print('\n----------DF ,Transpose dict.get()-,轉置------------------')
budget_t=budget_df.T
print(budget_t)

#索引,欄名
print("budget 索引：",budget_t.index)
print("budget 索引視為陣列：",budget_t.index.array)
print("budget 欄名：",budget_t.columns)

print("\n--------前5筆--------")
print(budget_t.head(5))


print("\n--------後5筆--------")
print(budget_t.tail(5))

print('\n---------取某個索引值,由0開始---------------')
row=budget_t.iloc[2]
print(row)

print('\n---取『值』---欄位---------------')
col=budget_t['值']
print(col)
print("type:",type(col))# <class 'pandas.core.series.Series'>

print("\n------資料串接(Concatenation)----------------------")

y_111=pd.DataFrame({
    "seq":16,
    "資料年度":"111年度",
    "統計項目":"歲出預算執行率",
    "資料單位":"％",
    "值":"98.99"
},index=[15])


print("111年度的預算資料：\n",y_111)