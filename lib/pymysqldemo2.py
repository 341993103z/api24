#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/18 17:11
# Author : smart
# @File : demo2.py
# @Software : PyCharm
import pymysql
try:
    con=pymysql.connect(host="localhost",port=3306,
                    user="root",password="root",
                    database="mysql",charset="utf8")
    cursor = con.cursor()
    cursor.execute("select * from user")
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print("出错了，错误信息为{}".format(e))
finally:
    if cursor:cursor.close()
    if con:con.close()
