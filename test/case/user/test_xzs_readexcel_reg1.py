#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/26 9:37
# Author : smart
# @File : test_xzs_readexcel_reg1.py
# @Software : PyCharm
import unittest,requests,json
from lib.read_excel import *
from lib.db import *
from lib.case_log import log_case_info


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.li=read_excel().excel_to_list(data_file, "TestUserReg")

    def test_reg_ok(self):
        case_data=read_excel().get_test_data(self.li,"reg_ok")
        url = case_data.get("url")
        args=case_data.get("args")
        exp=case_data.get("expect_res")
        a=json.loads(args).get("userName")
        if check_user(name=a):
            del_user(a)
        res=requests.post(url=url,json=json.loads(args))
        log_case_info("test_reg_ok",url,args,exp,res.text)
        self.assertIn(exp,res.text)
        del_user(a)

    def test_reg_err(self):
        case_data = read_excel().get_test_data(self.li, "reg_err")
        url = case_data.get('url')
        args = case_data.get('args')
        exp = case_data.get('expect_res')
        res=requests.post(url=url,json=json.loads(args))
        log_case_info("test_reg_err",url,args,exp,res.text)
        self.assertIn(exp,res.text)

if __name__ == '__main__':
    unittest.main()