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

def cre_tb2(name,db_name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db= ''+db_name+'')
    a = conn.cursor()
    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,username text, nameofdb text)"
    a.execute(sql)
    conn.commit()
    conn.close()
cre_tb2('b','mike')
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
    
def ins_blank2(name,n,a1,a2,a3,a4,a5,a6,a7):
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
 
def mike(name):
    na = name
    data_stock = read_web(na)
#print()
#na2 = input('name:')
#data2 = read_web(na2)
#print(data2)
    cre_tb(na)
    n = len(data_stock[0])
    data_list1 = []
    for i in range(9):
        data_list1.append([])
    for i in range(9):
        for j in range(n):
            data_list1[i].append(data_stock[0].iloc[j,i])
#print(data_list)
    for i in range(n):
        ins_blank(na,i,data_list1[0][n-1-i],str(data_list1[1][n-1-i]),str(data_list1[2][n-1-i]),str(data_list1[3][n-1-i]),str(data_list1[4][n-1-i]),str(data_list1[7][n-1-i]),str(data_list1[8][n-1-i]))
#name = input('name:')
#cre_tb(name)
#name1 = input('name:')
#cre_db(name1)
#ins_blank('m1',1,9,9,9,9,9,9,9)
        
name_s =['AAV', 'ADVANC', 'AMATA', 'ANAN', 'AOT', 'AP',
         'BA', 'BANPU', 'BBL', 'BCH', 'BCP', 'BCPG', 'BDMS',
         'BEAUTY', 'BEC', 'BEM', 'BH', 'BIG', 'BJC', 'BLAND',
         'BPP', 'BTS', 'CBG', 'CENTEL', 'CHG', 'CK', 'CKP', 'COM7',
         'CPALL', 'CPF', 'CPN', 'DTAC', 'EA', 'EGCO', 'EPG', 'ESSO',
         'GFPT', 'GGC', 'GLOBAL', 'GPSC', 'GUNKUL', 'HANA', 'HMPRO',
         'INTUCH', 'IRPC', 'ITD', 'IVL', 'JMART', 'JWD', 'KBANK', 'KCE',
         'KKP', 'KTB', 'KTC', 'LH', 'LPN', 'MAJOR', 'MC', 'MEGA', 'MINT',
         'MONO', 'MTC', 'ORI', 'PSH', 'PSL', 'PTG', 'PTT', 'PTTEP', 'PTTGC',
         'QH', 'ROBINS', 'SAWAD', 'SCB', 'SCC', 'SGP', 'SIRI', 'SPALI',
         'SPRC', 'STA', 'STEC', 'SUPER', 'TASCO', 'TCAP', 'THAI',
         'THCOM', 'TISCO', 'TKN', 'TMB', 'TOP', 'TPIPL', 'TPIPP',
          'TTA', 'TU', 'TVO', 'UNIQ', 'UV', 'WHA', 'WHAUP', 'WORK']

name_s2 = ['ADVANC', 'ANAN', 'AP', 'BA', 'BBL', 'BLAND',
           'CPF', 'EGCO', 'HANA', 'INTUCH', 'KKP', 'KTB',
           'KTC', 'LH', 'LPN', 'MC', 'PTT', 'PTTGC', 'QH',
           'SCB', 'SCC', 'SIRI', 'SPALI', 'TASCO', 'TCAP',
           'THCOM', 'TISCO', 'TMB', 'TU', 'TVO']

def f_01():
    from time import sleep
    for i in range(len(name_s)):
        mike(name_s[i])
        print(i)
        sleep(10)

def f_02():
    from time import sleep
    for i in range(len(name_s2)):
        mike(name_s2[i])
        print(i)
        sleep(10)
        
def setup():
    cre_db('setting')
    n0 = input('name_User')
    n1 = input('name_database')
