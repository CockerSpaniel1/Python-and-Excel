import pandas as pd
from datetime import date,datetime

df=pd.DataFrame(
    [
        [date(2024,8,1),date(2024,9,1)],
        [datetime(2024,9,1,10,20,5),datetime(2024,9,5,10,20,5)]
    ],
    index=['日期','日期時間'],
    columns=['起始','終止']
)

with pd.ExcelWriter("mydate.xlsx",
                    date_format="YYYY-MM-DD",
                    datetime_format="YYYY-MM-DD HH:MM:SS") as writer:
    df.to_excel(writer)
    

