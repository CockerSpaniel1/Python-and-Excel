import os
import time as t
import csv

customers = [ {"Name":"哈士奇", "Time":"2024/08/08 18:30","Order":"001"},
            {"Name":"約克夏", "Time":"2024/08/08 18:45","Order":"002"},
            {"Name":"米克斯", "Time":"2024/08/08 19:00","Order":"003"},
            {"Name":"吉娃娃", "Time":"2024/08/08 19:15","Order":"004"} ]


if (os.path.exists("Document")):    
    pass
else:
    os.mkdir("Document")

now = t.localtime(t.time())
str_today = t.strftime('%Y%m%d', now)
file_name = f'Document\\sale{str_today}.txt'

def return_dict(**kwargs):
    return kwargs

#逐筆寫入的函式
def write_text(cust_dict):
    with open(file_name,'a') as wf:
        for key in cust_dict.keys():
            value = cust_dict.get(key)
            wf.write(value+"\t")
        wf.write("\r\n")


if not (os.path.exists(file_name)):    
    with open(file_name,'w') as wf:
        wf.write("名稱\t時間\t編號  \r\n")
        wf.write("-------初始時加入的多筆資料-------------\r\n")
        for cust in customers:
            for key in cust.keys():
                value = cust.get(key)
                wf.write(value+"\t")

            wf.write("\r\n")
        wf.write("-------之後逐筆加入的資料-------------\r\n")

            
write_text({"Name":"米格魯", "Time":"2024/08/08 19:30","Order":"005"})
write_text({"Name":"雪納瑞", "Time":"2024/08/08 19:45","Order":"006"})
write_text(return_dict(Name="大麥町", Time="2024/08/08 20:00",Order="007"))


with open(file_name,'r') as rf:
    r = rf.read()
    path =  os.path.abspath(file_name)
    print(f'從路徑{path}的檔案內讀取出下方資料')
    print(r)