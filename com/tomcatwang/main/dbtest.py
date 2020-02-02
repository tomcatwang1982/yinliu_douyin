# -*- coding: utf-8 -*-
from com.tomcatwang.db.db import Database

#import pymysql

conf = {'host':'localhost','port':3306,'user':'root','pw':'123456','db':'yinliu','charset':'utf8'}
db = Database(conf)
result = db.query("select * from process")
for i in result :
    print(i)
#conn = pymysql.connect("localhost","root","123456","yinliu" )
'''
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='yinliu',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

conn = pymysql.connect(
    conf['host'],
    conf['user'],
    conf['pw'],
    conf['db'],
    cursorclass=pymysql.cursors.DictCursor)
'''


