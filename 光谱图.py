#import numpy as np
import pylab as pl
import xlrd as xl
file=xl.open_workbook('c4h10.xlsx')#打开表格，file为excel文件对象
table=file.sheets()[0]#按序号获取excel工作表，sheets（）返回一个列表，由下表指定工作表
wave=table.col_values(0)#按列获取工作表数据，第一列是波长
intensity=table.col_values(1)#按列获取工作表数据，第二列是强度，以后同理，每两列为一组（波长，强度）
pl.plot(wave, intensity)#绘图
pl.show()#显示图像
