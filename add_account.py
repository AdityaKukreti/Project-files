import mysql.connector
from random import randint

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def add_account():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
   
    name = input('Enter Name :')
    addr = input('Enter address ')
    phone = input('Enter Phone no :')
    email = input('Enter Email :')
    aadhar = input('Enter AAdhar no :')
    actype = input('Account Type (saving/current ) :')
    balance = input('Enter opening balance :')
    acno = randint(1111111111111111,9999999999999999)
    print()
    print("Thank you for creating an account!!")
    print()
    print("Your account no. is- " + str(acno))
    print()
    cursor.execute("""insert into `customer` values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(acno,name,addr,phone,email,aadhar,actype,'active',balance))
    conn.commit()
    conn.close()
    wait= input('\n\n\n Press any key to continue....')
