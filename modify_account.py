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


def modify_account():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    acno = input('Enter customer Account No :')
    print('Modify screen ')
    print('\n 1.  Customer Name')
    print('\n 2.  Customer Address')
    print('\n 3.  Customer Phone No')
    print('\n 4.  Customer Email ID')
    print()
    choice = int(input('What do you want to change ? '))
    if choice == 1:
        new_val = input('Enter your new name- ')
        cursor.execute("""update `customer` set `name` = %s where acno = %s""",(new_val,acno))
    if choice == 2:
        new_val = input('Enter your new address- ')
        cursor.execute("""update `customer` set `address` = %s where acno = %s""",(new_val,acno))
    if choice == 3:
        new_val = input('Enter your new phone no- ')
        cursor.execute("""update `customer` set `phone` = %s where acno = %s""",(new_val,acno))
    if choice == 4:
        new_val = input('Enter your new email id- ')
        cursor.execute("""update `customer` set `email` = %s where acno = %s""",(new_val,acno))
    
    conn.commit()
    print('\n\nCustomer Information modified..')
    wait = input('\n\n\n Press any key to continue....')
