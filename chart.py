#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author caoxm-me
# Email
# Date

# Contributor YongXin SHI <shiyongxing@aliyun.com>
# Last_update_time_at 2017/4/29


# pylab 在 python-matplotlib 模块中
import pylab as pl

import xlrd as xl

#import sourcedata
#da = sourcedata.Data()

def open_excel(file= 'file.xls'):
    try:
        data = xl.open_workbook(file)
        return data
    except Exception.e:
        print(str(e))

def predata(data):
    temp = []
    for i in (range(len(data)-2)):
        if not data[i+2] < data[i+1] > data[i]:

            temp.append(i+1)
            #print(temp)
            #data[i+1] = 0
    for i in temp:
        data[i] = 0
    return data

def runa(data):
    i = 0
    print(i)
    while i < 100:
        data = predata(data)
        i = i+1
        print(i)
    return data


def draw_chart(num):

    # 打开表格，file为excel文件对象
    file = open_excel('c4h10.xlsx')

    # 按序号获取excel工作表，sheets（）返回一个列表，由下表指定工作表
    table = file.sheets()[0]

    # 按列获取工作表数据，第一列是波长
    wave = table.col_values(0)

    # 按列获取工作表数据，第二列是强度，以后同理，每两列为一组（波长，强度）
    intensity = table.col_values(num)
    #print(intensity)
    # 绘图
    pl.plot(wave, runa(intensity))


for num_n in [1, 3, 5, 7, 9]:
    #print(num_n)
    draw_chart(num_n)

# 显示图像
pl.show()
pl.close()
