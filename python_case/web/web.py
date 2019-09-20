# # * coding:utf 8 *
# import urllib.request as request #網路連線
# import json
#
# src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
#
# with request.urlopen(src)as response:
# 	data=json.load(response) #利用json 模組處理 json y 資料格式
# #print(data)
# #clist=data["result"]["results"]
# #print(clist)
# #for company in clist:
# #    print(company["公司名稱"])
#
# clist=data["result"]["results"]
# with open("data.txt", "w", encoding="utf-8")as file:
#     for company in clist:
#         file.write(company["公司名稱"]+"\n")
from datetime import datetime

y_n = input('Enter your name: ')
print(f'Hello {y_n}!')

now = datetime.now()
print("now =", now)
