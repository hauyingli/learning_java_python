
# * coding:utf 8 *
import urllib.request as request #網路連線


src="https://tw.stock.yahoo.com/d/i/rank.php?t=vol&e=tse&n=100"

with request.urlopen(src) as response:
    data=response.read()
    print(data)

import bs4