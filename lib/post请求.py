#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/15 8:49
# Author : smart
# @File : post请求.py
# @Software : PyCharm
import requests

url = "http://192.168.55.22/zentao/user-login.html"

header={
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
data={
    'username':'admin',
    'password':'085445b9c180fe4bfd7368777580336c',
    'verifyRand':'1737660935'
}
r = requests.post(url,data)
print(r.text)