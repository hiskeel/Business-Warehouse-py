import os
import csv
id = 1
def main_menu():
    os.system('cls')
    choice = input("\n\nEnter menu point which u want:\n1. Work with warehouse\n2. Search for order\n3. Work with products\n4. Work with orders\n5. Save changes to file\n\n0. Exit program\n")
    os.system('cls')
    return choice
def warehouse_menu():
    os.system('cls')
    choice = input("Next step:\n1. Show all products in warehouse\n2. Sort products by group\n3. Sort products by price\n\n9. Back\n0. Exit program\n")
    os.system('cls')
    return choice
def search_menu():
    os.system('cls')
    choice = input("Next step:\n1. Search by name\n2. Search by group\n3. Search by phone number\n4. Search by destination\n5. Search by date\n\n9. Back\n0. Exit\n")
    os.system('cls')
    return choice
def product_menu():
    os.system('cls')
    choice = input("Next step:\n1. Change quantity\n2. Edit product info\n3. Add new product\n4. Delete product\n\n9. Back\n0. Exit\n")
    os.system('cls')
    return choice
def orders_menu():
    os.system('cls')
    choice = input("Next step:\n1. Show orders\n2. Add new order\n3. Edit order\n4. Delete order\n\n9. Back\n0. Exit\n")
    os.system('cls')
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
    id = input("Enter id of product you want to edit: ")
    with open('products_DB.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)

    # Update the information about the object
        for row in my_list:
            if row[0] == id:
                row[0] = int(input("Enter new id: "))
                row[1] = input("Enter new group: ")
                row[2] = input("Enter new name: ")
                row[3] = int(input("Enter new price: "))
                row[4] = int(input("Enter new quantity: "))
                with open('products_DB.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(my_list)
                    file.close()
    csv_file.close()

def Delete_product():
    show_products()
    id = input("Enter id of product you want to DELETE: ")
    with open('products_DB.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)

        count = 0
        for row in my_list:
            if row[0] == id:
                my_list.pop(count)
                with open('products_DB.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(my_list)
                    file.close()
            count += 1
    csv_file.close()
    return 0
def Change_quantity():
    show_products()
    id = input("Enter id of product you want to edit quantity: ")
    with open('products_DB.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)

    # Update the information about the object
        for row in my_list:
            if row[0] == id:
                row[4] = input("Enter new quantity: ")
                with open('products_DB.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(my_list)
                    file.close()
    csv_file.close()
def Sort_products_by_price():
    show_products()
    confirm = input("Are you sure you want to sort products by price:\n1. Yes\n2. No\n")
    if confirm == '1':
        with open('products_DB.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            my_list = list(reader)
            i = 1  
            while(i < my_list.__len__()):
                it = 1
                while(it < my_list.__len__()):
                    if my_list[i][3] <= my_list[it][3]:
                        temp = my_list[i]
                        my_list[i] = my_list[it]
                        my_list[it] = temp
                    it +=1
                i += 1
            csv_file.close()
            with open('products_DB.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(my_list)
                file.close()

        print("Products list, sucessfully sorted by price!")
def sort_by_group():
    show_products()
    confirm = input("Are you sure you want to sort products by price:\n1. Yes\n2. No\n")
    if confirm == '1':
        with open('products_DB.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            my_list = list(reader)
            i = 1  
            while(i < my_list.__len__()):
                it = 1
                while(it < my_list.__len__()):
                    if my_list[i][1] <= my_list[it][1]:
                        temp = my_list[i]
                        my_list[i] = my_list[it]
                        my_list[it] = temp
                    it +=1
                i += 1
            csv_file.close()
            with open('products_DB.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(my_list)
                file.close()

        print("Products list, sucessfully sorted by Group!")


       
            
        
