#------上課內容--------------------------------------------------------------------------------------------------------------
import pandas as pd 

order = pd.DataFrame()
d = pd.read_excel('order.xlsx', sheet_name=None)
s = pd.ExcelFile('order.xlsx')

for name in s.sheet_names:
    order=pd.concat([order, d.get(name)] , ignore_index=True)

#------作業--------------------------------------------------------------------------------------------------------------
order['金額'] = order['數量'] * order['單價']

#各類別合計
df_catogory = order.groupby('類別')[['數量','金額']].sum().rename(columns={"金額":"金額合計"}) 
df_catogory.loc["總計"] = ["" , df_catogory['金額合計'].sum()]
print(df_catogory)

#各產品合計
df_product = order.groupby(['類別', '產品名稱' ])[['數量', '金額']].sum() #產生MultiIndex,=>[(level=0, 1)] [('穀類麥片', 再來米)]
df_price = order.groupby(['類別', '產品名稱' ])['單價'].mean().to_frame() #取得和上面index相同列數的 產品單價Series後轉成DF 
                                                                         # (因為上面的單價會被加總，用這方式取得固定的價格)  
df_product = df_price.merge(df_product,left_index=True, right_index=True) #將兩個DataFrame左右合併 (相同列數但新增一單價欄位)

index_names = df_product.index.get_level_values(level="類別").unique()
print(df_product)

with pd.ExcelWriter("retail.xlsx", engine="openpyxl") as writer:
    df_catogory.to_excel(writer, sheet_name="類別加總") #首頁
    
    for category in index_names:
        df_sheet = df_product.loc[category].sort_values("金額" ,ascending=False)
        df_sheet.loc["合計"] = [ "" , "" , df_sheet['金額'].sum() ] #添加新列只能用loc ,用iloc會Index error

        df_sheet.to_excel(writer,sheet_name=category)

print("檔案 retail.xlsx 建立成功")