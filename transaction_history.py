import mysql.connector
from datetime import date

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def clear():
    for _ in range(65):
        print()


def transaction_report():
    clear()
    
    conn = mysql.connector.connect(host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    acno = input('Enter your account no. - ')
    print()
    cursor.execute("""select * from `transaction` where `acno` = %s""",(acno,))
    print('-' * 85)
    print('Transaction id', end = '  | ')
    print('Date of transaction', end = '  | ')
    print('Amount', end = '    | ')
    print('Type', end = '      | ')
    print('Account number')
    print('-' * 85)
    for i in cursor:
        print(i[0], end = '')
        for j in range(18 - len(str(i[0]))):
            print(' ', end = '')
        print(i[1], end = '')
        for j in range(23 - len(str(i[1]))):
            print(' ', end = '')
        print(float(i[2]), end = '')
        for j in range(10 - len(str(i[2]))):
            print(' ', end = '')
        print(i[3], end = '')
        for j in range(12 - len(i[3])):
            print(' ', end = '')
        print(i[4])
    print('-' * 85)
    wait = input('\n\n\n Press any key to continue....')

