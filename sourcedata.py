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

def data(num = 1):
    # 打开表格，file为excel文件对象
    file = open_excel('c4h10.xlsx')

    # 按序号获取excel工作表，sheets（）返回一个列表，由下表指定工作表
    table = file.sheets()[0]

    # 按列获取工作表数据，第一列是波长
    wave = table.col_values(0)

    # 按列获取工作表数据，第二列是强度，以后同理，每两列为一组（波长，强度）
    intensity = table.col_values(num)

    #print(wave)
    data = [[],[]]
    data[0] = wave
    data[1] = intensity

    return data


# 行和列交换
def source(data):
    return list(list(i) for i in zip(*data))

# 滤波
def wave_filtering(daa):
    m = (max(daa[1])-min(daa[1]))*0.6+min(daa[1])
    med = (max(daa[1])-min(daa[1]))*0.5+min(daa[1])

    data = source(daa)

    for num in range(len(data)):
        if data[num][1] < m:
            data[num][1] = 3000

    data = source(data)
    return data
