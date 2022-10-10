import mysql.connector as sql
import pandas as pd
conn=sql.connect(host='localhost',user='root',passwd='',database='grocery_shop')
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()


print('General Store Management System')
print('1.login')
print('2.exit')
choice=int(input('enter the choice : '))
if choice==1:
    user_name=input('enter the user name = ')
    password=input('enter the password = ')
    while user_name=='' and password=='':
        print('yayyy connected successfully')   

        print('*'*21)
        print('    General Store')
        print('*'*21)
        print('1.Insert customer details')
        print('2.Insert product details') 
        print('3.Insert worker details')
        print('4.See all customer details')
        print('5.See all product details')
        print('6.See all worker details')
        print('7.Export Customer Data to csv')
        print('8.Export Product Data to csv')
        print('9.Export Workers Data to csv')
        print('10.pie chart for avalibility of stock')
        print('11.exit')

        choice=int(input('Enter the choice : '))
        if choice==1:
            cust_name=input('Enter the Name of Customer = ')
            phone_no=int(input('Enter the phone number = '))
            cost=float(input('Enter the item cost purchased = '))
            sql_insert="insert into customer_details values("+str(phone_no)+",'"+(cust_name)+"',"+str(cost)+")"
            c.execute(sql_insert)
            conn.commit()
            print('Data is updated')


        elif choice==2:
            product_name=input('Enter  product name = ')
            product_cost=float(input('Enter the cost = '))
            qty = int(input('Enter the Quantity of the item = '))
            sql_insert="insert into product_details values(""'"+(product_name)+"',"+str(product_cost)+","+str(qty)+")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')


        elif choice==3:
            worker_name=input('Enter the name = ')
            worker_work=input('Enter the work = ')
            worker_age = int(input('Enter the age = '))
            worker_salary = float(input('enter the salary = '))
            phone_no = int(input('enter the  phone number = '))
            sql_insert = "insert into worker_details values(" "'"+(worker_name)+"'," "'"+(worker_work)+"',"+str(worker_age)+","+str(worker_salary)+","+str(phone_no)+ ")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')


        elif choice==4:
            print('1. Show all customers details')
            print('2. Show specified Customer Details')
            cd = int(input('Enter your choice : '))
            if cd == 1 : 
                query = 'select *from customer_details'
                display = pd.read_sql(query, conn)
                print()
                print(display)
                print()
            
            if cd == 2: 
                pinput = input('Enter Name of the Customer = ')
                qry = 'select *from customer_details where cust_name  = ''\''+(pinput)+'\';'
                # print(qry)
                print()
                display = pd.read_sql(qry, conn)
                print(display)
                print()
                

        elif choice==5:
            print('1. Show all product details')
            print('2. Show specified product Details')
            cd = int(input('Enter your choice : '))
            if cd == 1 : 
                query = 'select *from product_details'
                display = pd.read_sql(query, conn)
                print()
                print(display)
                print()
            
            if cd == 2 : 
                pinput = input('Enter Name of the product = ')
                qry = 'select *from product_details where product_name = ''\''+(pinput)+'\';'
                # print(qry)
                display = pd.read_sql(qry, conn)
                print()
                print(display)
                print()

        elif choice==6:
            print('1. Show all worker details')
            print('2. Show specified worker Details')
            cd = int(input('Enter your choice : '))
            if cd == 1 : 
                query = 'select *from product_details'
                display = pd.read_sql(query, conn)
                print()
                print(display)
                print()
            
            if cd == 2 : 
                pinput = input('Enter Name of the product = ')
                qry = 'select *from product_details where product_name = ''\''+(pinput)+'\';'
                # print(qry)
                display = pd.read_sql(qry, conn)
                print(display)

        elif choice==7:
            print('*'*20)
            f=open('test.txt','r')
            data=f.read()
            print(data)
            
            f.close()
            print('*'*20)

        elif choice==11:
            import matplotlib.pyplot as plt
            items=('shoes','stationary','watch','house use','food items')
            avalibility=[156,200,103,206,196]
            colors=['red','yellowgreen','blue','gold','green']
            plt.pie(avalibility,labels=items,colors=colors)
            plt.title('avalibility of items in shop')
            plt.show()

        elif choice==12:
            exit()
            
    else:
        print('wrong password, try again ')
        
            
if choice==2:
    exit()





# "'"+(product_name)+"',"+str(product_cost)+","+str(qty)+
# '\''+(pinput)+'\';'



