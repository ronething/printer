#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql
import json

print('Content-Type: text/html')
print() #空行，告诉服务器结束头部
# 打开数据库连接

db = pymysql.connect("localhost","user","password","linux")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句

sql = "select * from demo";

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    dic = {}
    for row in results:
        dic[row[0]] = row[1]

    print(json.dumps(dic))
except:
    print("Error:unable to fecth data")

# 关闭数据库连接
db.close()


