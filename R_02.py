# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:07:09 2018

@author: wuttinun_r
"""
import mysql.connector
import pandas as pann
data = pann.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SETHD&language=th&country=TH')
print(data[2])
print(len(data))
name = data[2]
#name1 = []
#for i in range(len(name)):
#    name1.append(name[i][1])
def cre_tb(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='mike1')
    a = conn.cursor()
    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,date text, open text,max text,min text,close text,vol text,val text)"
    a.execute(sql)
    conn.commit()
    conn.close()

    
#print(type(name))
#data1 = tuple(name)
#print(name.iloc[1][0])
na_stock = []
for i in range (len(name)):
    na_stock.append(name.iloc[i][0])    
print(na_stock)

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
#print(type(name_s))