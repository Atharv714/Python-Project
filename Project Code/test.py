import mysql.connector as sql
import pandas as pd
atharv = sql.connect(host = 'localhost', user = 'root', passwd = 'atharvrastogi9', database = 'test')
if atharv.is_connected():
    letter = input("Enter the initial letter : ")
    query = "select *from student where names like '%s%%' ;" %(letter,)
    marks = pd.read_sql(query, atharv)
    print()
    print(marks)
    print()