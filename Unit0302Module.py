#匯入自訂模組
import fruit
from shop.cake import current   #匯入current 函數
import vegatable as vg #匿稱


#使用fruit 模組內的自訂函數
fruit.favorite("香蕉")
fruit.sale("Mango",120)
fruit.onsale("櫻桃",300,800,20)
fruit.onsale("巴樂",50,120,10)
fruit.dessert("綜合水果起司蛋糕","蘋果派","香蕉蛋糕")

product={
    "蘋果派":{
        "編號":1,
        "價格":100,
        "卡洛里":500,
        "供應商":"爭甜"
    },
    "綜合水果起司蛋糕":{
        "編號":2,
        "價格":200,
        "卡洛里":800,
        "供應商":"布甜"
    },
    "香蕉蛋糕":{
        "編號":3,
        "價格":90,
        "卡洛里":200,
        "供應商":"爭甜"
    }
}

fruit_cake={
    "鳯山":{
        "蓮蓉":1000,
        "桂圓":950,
        "綠豆踫":500,
        "水果":650
    },
    "新興":{
        "蓮蓉":1000,
        "桂圓":950,        
        "水果":650
    },
    "巨蛋":{
        "蓮蓉":1000,
        "桂圓":950,
        "綠豆踫":500       
    }
}


fruit.detail(product)
fruit.dessert(fruit_cake)

current("餅乾","蛋糕")

vg.organic("高麗菜",10,250)

