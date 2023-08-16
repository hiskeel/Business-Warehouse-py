import os
import csv



def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = input("WELCOME!\n\nEnter menu point which u want:\n1. Work with warehouse\n2. Search for order\n3. Work with products\n4. Work with orders\n5. Save changes to file\n0. Exit program\n")
    return choice
def warehouse_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = input("Next step:\n1. Show all products in warehouse\n2. Sort products by group\n3. Sort products by price\n9. Back\n0. Exit program\n")
    return choice
def search_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = input("Next step:\n1. Search by name\n2. Search by group\n3. Search by phone number\n4. Search by destination\n5. Search by date\n9. Back\n0. Exit\n")
    return choice
def product_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = input("Next step:\n1. Change quantity\n2. Edit product info\n3. Add new product\n4. Delete product")
    return choice

exit_program = False
back = False

while (exit_program != True):
    
