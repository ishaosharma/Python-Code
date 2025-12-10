import pymysql

con = pymysql.connect(host='localhost', user = 'root', password='root', db = 'demoo')
print("**Database connection established**")

cursor=con.cursor 