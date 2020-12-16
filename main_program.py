import mysql.connector
from datetime import date
from add_account import add_account
from modify_account import modify_account
from close_account import close_account
from activate_account import *
from transaction_menu import transaction_menu
from search_menu import search_menu
from transaction_history import transaction_report



def main_menu():
    while True:
      clear()
      print(' Main Menu')
      print("\n1.  Add Account")
      print('\n2.  Modify Account')
      print('\n3.  Close Account')
      print('\n4.  Activate Account')
      print('\n5.  Transaction Menu')
      print('\n6.  Search Account')
      print('\n7.  Transaction History')
      print('\n8.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_account()
      if choice == 2:
        modify_account()
      if choice == 3:
        close_account()

      if choice == 4:
        activate_account()

      if choice ==5 :
        transaction_menu()
      if choice ==6 :
        search_menu()
      if choice == 7:
        transaction_report()
      if choice ==8:
        print()
        print('Thank you for using the application!! We hope you have a great day!')
        print()
        print('Exiting...')
        print()
        break


main_menu()