#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/15 10:23
# Author : smart
# @File : zhj.py
# @Software : PyCharm
import requests
kw = "原神"
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="
header = {
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
params = { "ie": "utf-8","q": kw}
rep = requests.get(url, headers=header, params=params)
rep.encoding = "utf-8"
# print(rep.status_code)
# print(rep.url)
print(rep.headers)
# print(rep.cookies)
# print(rep.text)
# print(rep.content)