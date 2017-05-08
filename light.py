#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author YongXin SHI
# Email shiyongxin@aliyun.com
# Date 2016/11/07

# Last_update_time_at 2017/4/30


import numpy as np

##(x,y)
#input_date=[(3,90),(4,68),(5,38),(6,18),(7,8),(8,3),(9,5),(10,48)]
#lib_date=[(1,5),(2,48),(3,98),(4,68),(5,38),(6,18),(7,8),(8,2)]


################################################
import sourcedata

def data(num = 1):
    # 打开表格，file为excel文件对象
    file = sourcedata.open_excel('c4h10.xlsx')

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

daa = data()

# sourcedata.source  行和列交换
input_date = sourcedata.source(data())
lib_date = sourcedata.source(data(3))

# 滤波
def wave_filtering(daa):
    m = (max(daa[1])-min(daa[1]))*0.6+min(daa[1])
    med = (max(daa[1])-min(daa[1]))*0.5+min(daa[1])

    data = sourcedata.source(daa)

    for num in range(len(data)):
        if data[num][1] < m:
            data[num][1] = 3000

    data = sourcedata.source(data)
    return data

input_date = wave_filtering(data())
lib_date = wave_filtering(data(3))
#print(input_date)

import pylab as pl
pl.plot(input_date[0], input_date[1])
pl.plot(lib_date[0], lib_date[1])

# 显示图像
pl.show()
pl.close()

input_date = sourcedata.source(input_date)
lib_date = sourcedata.source(lib_date)

#################################

##二位数组降到一维
def reduction(inputdate):
    n=0
    in_date=[]
    while n < len(inputdate):
        in_date.append(inputdate[n][1])
        n = n + 1
    return in_date

def multi():
    pass

def cutheader(date):
    return date[1:len(date)]

def cutfooter(date):
    return date[0:len(date)-1]

##
##去掉无用数据
##select == 0 return input_date
##select == 1 return lib_date
def draw(input_date,lib_date,select):
    reduction(input_date)
    reduction(lib_date)

    while input_date[0][0] > lib_date[0][0]:
        lib_date = cutheader(lib_date)
    while input_date[0][0] < lib_date[0][0]:
        input_date = cutheader(input_date)
    while input_date[len(input_date)-1][0] > lib_date[len(lib_date)-1][0]:
        input_date = cutfooter(input_date)
    while input_date[len(input_date)-1][0] < lib_date[len(lib_date)-1][0]:
        lib_date = cutfooter(lib_date)
    if select == 0:
        return input_date
    elif select == 1:
        return lib_date
    else:
        return "seletc error select == 0 or 1"

##计算波形误差
##均方误差（MSE）
def similarity(input_date,lib_date):
    n=0
    sumsum=0
##    dvalue=[]
##    ddvalue=[]
##    dddvalue=[]
##    sum=0
    while n < len(lib_date):
        sumsum = sumsum + (input_date[n][1]-lib_date[n][1])*(input_date[n][1]-lib_date[n][1])
##
##
####        print((input_date[n][1]-lib_date[n][1])*(input_date[n][1]-lib_date[n][1]))
##        dvalue.append((input_date[n][1]-lib_date[n][1])^2)
####        print(dvalue)
##
##        ddvalue.append(lib_date[n][1]-dvalue[n])
####        print(ddvalue)
##
##        dddvalue.append(ddvalue[n]/lib_date[n][1])
####        print(ddvalue[n]/lib_date[n][1])
##        sum=dddvalue[n]+sum
        n = n + 1
##    print(sum/len(lib_date))
##    return sum/len(lib_date)
    return sumsum/len(lib_date)


##
##判断波形是否相等
##如果相等 return 0
##如果不想等 return 1

def contrast(input_date,lib_date):
    print(input_date)
    print(lib_date)
##    print(input_date.__len__())
##    for num in input_date[*][1]:
##        print(num)
##    print(input_date-lib_date)


    return 0


##contrast(input_date,lib_date)
##draw(input_date,lib_date,1)
#print(draw(input_date,lib_date,0))
#print(draw(input_date,lib_date,1))

print(similarity(draw(input_date,lib_date,0),draw(input_date,lib_date,1)))
