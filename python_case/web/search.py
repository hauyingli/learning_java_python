# * coding:utf 8 *
import urllib.request as request #網路連線


src="http://www.google.com"

with request.urlopen(src) as response:
    data=response.read().decode("utf-8")
    print(data)

import bs4



