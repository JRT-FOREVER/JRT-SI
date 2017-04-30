#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author YongXin SHI
# Email shiyongxin@aliyun.com
# Date 2016/04/30

import xlrd as xl


def open_excel(file= 'file.xls'):
    try:
        data = xl.open_workbook(file)
        return data
    except Exception.e:
        print(str(e))


def source(data):
    return list(list(i) for i in zip(*data))
