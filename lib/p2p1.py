#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/22 10:40
# Author : smart
# @File : p2p1.py
# @Software : PyCharm
import pymysql

#建立数据库的连接
def conn():
    conn =pymysql.connect(
        host='localhost',user='root',
        password='root',db='p2p',
        port=3306,charset='utf8'
    )
    return conn

#封装数据库的查询结果
def query_db(sql):
    #建立连接
    con = conn()
    #建立游标
    cur =con.cursor()
    #执行sql
    cur.execute(sql)
    #获取返回的查询结果
    result =cur.fetchall()
    return result

#封装数据库的更改操作
def chang_db(sql):
    # 建立连接
    con = conn()
    # 建立游标
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
        #提交更改
        con.commit()
    except Exception as e:
        #回滚
        con.rollback()
    # 获取返回的查询结果
    finally:
        #关闭游标
        cur.close()
        #关闭连接
        con.close()
#封装常用的数据库操作
#查询
def check_user(name):

    sql='select * from  t_user where user_name = "{}"'.format(name)
    result=query_db(sql)
    return True if result else False
#添加
def add_user(name,password):
    sql="insert into t_user(user_name,password) values ('{}','{}')".format(name,password)
    chang_db(sql)
#删除
def del_user(name):
    sql='delete from t_user where user_name="{}"'.format(name)
    chang_db(sql)