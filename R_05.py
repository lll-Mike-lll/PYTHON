# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:52:34 2018

@author: MIKE
"""

import pandas as pann
import mysql.connector 

def read_web(a):
    dt = pann.read_html('http://www.panphol.com/data/page/stockprice/'+a+'#')
#    print(dt)
#    print(type(dt[0]))
#    print(len(dt[0]))
    return dt

def se_db(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='mike1')
    cur = conn.cursor()
    sql = "SELECT * FROM "+name+" ORDER BY id"
    cur.execute(sql)
    row_db  = cur.fetchall()
#    print(row_db)
    print(type(row_db))
    n = len(row_db)
    print(len(row_db))
#    print(row_db)
    return row_db
    
    
def mike():
    dt_today = read_web('ptt')
    data =   se_db('ptt')
    data1 = []
    n= -1
    p=len(data)
    print(len(dt_today[0]))
    print(data[0][1])
#    for i in range(len(dt_today)):
##        data1.append(data[i][1])
#        if data[p]==dt_today[i]:
#            n=i
#    print(i)
        
#    print(data1)
    
    
mike()
   