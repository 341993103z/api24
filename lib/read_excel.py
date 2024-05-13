#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/23 16:53
# Author : smart
# @File : read_excel.py
# @Software : PyCharm
import xlrd
class read_excel():
    def excel_to_list(self,filename,sheetname):
        #打开excel文件
        wb = xlrd.open_workbook(filename)
        #打开工作簿
        sh = wb.sheet_by_name(sheetname)
        #创建一个空白列表
        list = []
        #根据第一行获取key值
        keys = sh.row_values(0)
        #循环 从第二行开始获取数据
        for i in range(1,sh.nrows):
            #获取每一行的数据
            v = sh.row_values(i)
            #根据key值和value值的列表合成一个字典并添加到空白列表中
            list.append(dict(zip(keys,v)))
            #返回列表
        return list

    #从全部用例数据中读取指定的用例数据
    def get_test_data(self,data_list,case_nmae):
        for case_data in data_list:
            #如果字典数据中case_name与参数一致
            if case_nmae == case_data['case_name']:
                #如果查询不到会返回None
                return case_data

if __name__ == '__main__':
    r = read_excel()
    l = r.excel_to_list("test_user_data.xlsx","test_user_login")
    print(l)
    print(r.get_test_data(l,"login_ok"))