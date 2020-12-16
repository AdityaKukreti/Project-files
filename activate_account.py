import mysql.connector
import time

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def clear():
    for _ in range(65):
        print()


def activate_account():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    acno = input('Enter customer Account No :')
    det = {}
    cursor.execute('select acno,status from customer')

    for i in cursor:
        det[i[0]] = i[1] 

    for i in range(len(det)):
        if acno not in det:
            print('No account with this account no. exists')
            wait= input('\n\n\n Press any key to continue....')
            break
        elif det[acno] == 'active':
            print('Account is already active')
            wait= input('\n\n\n Press any key to continue....')
            break
        elif  det[acno] == 'close':
            cursor.execute('update `customer` set `status` = "active" where acno = %s',(acno,))
            conn.commit()
            print('\n\nAccount Activated')
            wait= input('\n\n\n Press any key to continue....')
            break    