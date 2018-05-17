# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:11:00 2018

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
    data1 = read_web('ptt')
    data2 = se_db('ptt')
    n = len(data2)
    n2 = len(data1[0])
#    print(data2[0][1])
#    print(len(data1[0]))
#    print(n)
    print(data1[0].iloc[1][0])
    for i in range(n2):
        if data2[n-1][1] == data1[0].iloc[i][0]:
            print(i)

mike()