# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:07:09 2018

@author: wuttinun_r
"""
import pandas as pann
data = pann.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH')
#print(data[2])
print(len(data))
name = data[2]
#name1 = []
#for i in range(len(name)):
#    name1.append(name[i][1])
    
print(type(name))
data1 = tuple(name)
print(name.iloc[1][0])