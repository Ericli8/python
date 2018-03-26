#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect(
                     host = '127.0.0.1',  # 远程主机的ip地址， 
                     user = 'root',   # MySQL用户名
                     db = 'runoob',   # database名
                     passwd = '',   # 数据库密码
                     port = 3306,  #数据库监听端口，默认3306
                     charset = "utf8"
					 )  
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
# SQL 删除语句
sql = "INSERT INTO school(name, old) VALUES ('小红红', '28')"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()