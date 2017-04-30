#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author  caoxm-me  <caoxmme@outlook.com>
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


def data_pre(data):
    index = []           #存放索引
    for i in (range(len(data)-2)):
        if not (data[i+1]>data[i] and data[i+1]>data[i+2]):
            index.append(i+1)
    return index


def data_filter(data,index):
    # 过滤无效数据
    for i in index:
        data[i]=0
    def is_zero(x):
        return(x!=0)
    data=(list(filter(is_zero,data)))
    return data


def draw_chart(num):

    # 打开表格，file为excel文件对象
    file = open_excel('c4h10.xlsx')

    # 按序号获取excel工作表，sheets（）返回一个列表，由下表指定工作表
    table = file.sheets()[0]

    # 按列获取工作表数据，第一列是波长
    r_wave = table.col_values(0)
    # 按列获取工作表数据，第二列是强度，以后同理，每两列为一组（波长，强度）
    r_intensity = table.col_values(num)
    intensity_index=data_pre(r_intensity)
    intensity=data_filter(r_intensity,intensity_index)
    #print(type(intensity))
    print("filter y:",intensity)
    wave=data_filter(r_wave,intensity_index)
    print("filter x:", wave)
    #print(intensity)
    # 绘图
    pl.plot(wave, intensity)


for num_n in [1, 3, 5, 7, 9]:
    #print(num_n)
    draw_chart(num_n)

# 显示图像
pl.show()
pl.close()
