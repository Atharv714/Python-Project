import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='',database='grocery_shop')
if conn.is_connected():
    print('successfully connected')

c=conn.cursor()
c.execute('create table customer_details(phone_no long,cust_name varchar(25),cost float(10))')
print('table created')

c.execute('create table product_details(product_name varchar(25),product_cost float(10))')
print('table created')

c.execute('create table worker_details(worker_name varchar(25),worker_work varchar(10),worker_age int(3), worker_salary float(10),phone_no int(13))')
print('table created')

c.execute('Alter table product_details add qty int')
