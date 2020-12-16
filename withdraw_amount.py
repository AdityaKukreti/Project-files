import mysql.connector
from datetime import date
from account_status import *

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    


def clear():
    for _ in range(65):
        print()


def withdraw_amount():
    conn = mysql.connector.connect(host= h, database=d, user=u, password=p)
    cursor = conn.cursor()
    acno = input('Enter account No : ')
    amount = int(input('Enter amount to be withdrawed : '))
    today = date.today()
    result = account_status(acno)
    total = result[1] - float(amount)
    if result[0] == 'active' and result[1] >= float(amount):
        cursor.execute("""update `customer` set `balance` = %s where `acno` = %s""",(total,acno))
        cursor.execute("""insert into `transaction` (`dot`,`amount`,`type`,`acno`) values (%s,%s,%s,%s)""",(today,total,'withdraw',acno))
        conn.commit()
        print('\n\nAmount Withdrawn')
    
    elif result[0] == 'active' and result[1] <= float(amount):
        print('\n\nInsufficient amount')
    
    else:
        print('\n\nClosed or Suspended Account')

    wait = input('\n\n\n Press any key to continue....')
    conn.close()
