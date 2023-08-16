import os
import csv

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = int(input("WELCOME!\n\nEnter menu point which u want:\n1. Work with warehouse\n2. Search for order\n3. Work with products\n4. Work with orders\n5. Save changes to file\n\n0. Exit program\n"))
    return choice
def warehouse_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = int(input("Next step:\n1. Show all products in warehouse\n2. Sort products by group\n3. Sort products by price\n\n9. Back\n0. Exit program\n"))
    return choice
def search_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = int(input("Next step:\n1. Search by name\n2. Search by group\n3. Search by phone number\n4. Search by destination\n5. Search by date\n\n9. Back\n0. Exit\n"))
    return choice
def product_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = int(input("Next step:\n1. Change quantity\n2. Edit product info\n3. Add new product\n4. Delete product\n\n9. Back\n0. Exit\n"))
    return choice
def orders_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = int(input("Next step:\n1. Show orders\n2. Add new order\n3. Edit order\n4. Delete order\n\n9. Back\n0. Exit\n"))
    return choice

def show_products():
    with open('products_DB.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
        csv_file.close()
    return 0
def Add_product():
    with open('products_DB.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([int(input("Enter product id: ")), input("Enter product group: "), input("Enter product name: "), int(input("Enter product price: ")), int(input("Enter product quantity: "))])
        file.close()
    return 0
def Edit_product():
    show_products()
    id = int(input("Enter id of product you want to edit: "))
    with open('products_DB.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == id:
                with open('product_DB.csv', 'a', newline='') as file:
                    row[0] = int(input("Enter new id: "))
                    row[1] = input("Enter new group: ")
                    row[2] = input("Enter new name: ")
                    row[3] = int(input("Enter new price: "))
                    row[4] = int(input("Enter new quantity: "))
                file.close()

        csv_file.close()
