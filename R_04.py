# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:17:25 2018

@author: MIKE
"""
import mysql.connector
import pandas as pann

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
#    print(type(row_db))
#    n = len(row_db)
#    print(len(row_db))
    return row_db

row = se_db('ptt')
date_01 = []
for i in range(len(row)):
#    print(i)
#    date_01.append(row[1][i])
#    print(row[i][1])
    
    
