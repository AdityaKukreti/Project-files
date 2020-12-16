import mysql.connector

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def clear():
    for _ in range(65):
        print()

def search_menu():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    acno = input('Enter your account no. - ')
    ad_no = input('Enter your aadhar card no. - ')
    print()
    print()
    det = {}
    cursor.execute('select * from `customer`')
    
    for i in cursor:
        det[i[0]] = i[5]

    
    if acno in det:
        if det[acno] == ad_no:
            print('-' * 168)
            print('Account Number', end = '    | ')
            print('Customer Name', end = '    | ')
            print('Address', end = '              | ')
            print('Phone Number', end = '    | ')
            print('Email               ', end = '    | ')
            print('Aadhar Number', end = '    | ')
            print('Account Type', end = '    | ')
            print('Status', end = '    | ')
            print('Balance')
            print('-' * 168)
            cursor.execute('select * from `customer` where `acno` = %s',(acno,))
            for i in cursor:
                print(i[0], end = '')
                for j in range(20 - len(i[0])):
                    print(' ', end = '')
                print(i[1], end = '')
                for j in range(19 - len(i[1])):
                    print(' ', end = '')
                print(i[2], end = '')
                for j in range(23 - len(i[2])):
                    print(' ', end = '')
                print(i[3], end = '')
                for j in range(18 - len(i[3])):
                    print(' ', end = '')
                print(i[4], end = '')
                for j in range(26 - len(i[4])):
                    print(' ', end = '')
                print(i[5], end = '')
                for j in range(19 - len(i[5])):
                    print(' ', end = '')
                print(i[6], end = '')
                for j in range(18 - len(i[6])):
                    print(' ', end = '')
                print(i[7], end = '')
                for j in range(12 - len(i[7])):
                    print(' ', end = '')
                print(i[8])
            print('-' * 168)
    wait = input('\n\nPress any key to continue.......')
