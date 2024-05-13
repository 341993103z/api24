#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/22 10:48
# Author : smart
# @File : p2p_login.py
# @Software : PyCharm
import requests
class login():
    def login(self,user,ps):
        url = "http://192.168.55.22:8082/p2p_management/login "
        data ={"userName":user,"password":ps,"remember":False}
        r = requests.post(url,json=data)
        return r
if __name__ == '__main__':
    l =login()
    print(l.login("tom", "tom").text)
