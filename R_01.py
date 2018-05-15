# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:03:06 2018

@author: wuttinun_r
"""
import mysql.connector
import pandas as pann

def read_web(a):
    dt = pann.read_html('http://www.panphol.com/data/page/stockprice/'+a+'#')
#    print(dt)
#    print(type(dt[0]))
#    print(len(dt[0]))
    return dt

def cre_tb(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='mike')
    a = conn.cursor()
    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,date text, open text,max text,min text,close text,vol text,val text)"
    a.execute(sql)
    conn.commit()
    conn.close()
    
def cre_db(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='')
    a = conn.cursor()
    sql = "CREATE DATABASE "+name+";"
    a.execute(sql)
    conn.commit()
    conn.close()
    
def ins_blank(name,n,a1,a2,a3,a4,a5,a6,a7):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='mike')
    a = conn.cursor()
#    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,date text, open text,max text,min text,close text,vol text,val text)"
    sql = "INSERT INTO "+name+"(id,date,open,max,min,close,vol,val) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#    num = 1
#    add_db = (num,'pp','pp','pp','pp','pp','pp','pp')
    add_db = (n,a1,a2,a3,a4,a5,a6,a7)
    a.execute(sql,add_db)
#    a.execute(sql)
    conn.commit()
    conn.close()    
  
na = input('name:')
data = read_web(na)
print(data)

na2 = input('name:')
data2 = read_web(na2)
print(data2)
    
#name = input('name:')
#cre_tb(name)

#name1 = input('name:')
#cre_db(name1)
    
#ins_blank('m1',1,9,9,9,9,9,9,9)