import csv
import datetime

def search_by_name():
    s_name = input("Enter name of client you want to check orders: ")
    result = 0
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)
        for item in my_list:
            if item[2].upper() == s_name.upper():
                print(item)
                result += 1
        if result == 0:
            print(f"No such clients with name {s_name}!")

        csv_file.close()
    contin = input("Enter any symbol to continue:\n")
    return 0
def search_by_procces():
    s_request = input("Enter procces of orders you want to check: ")
    result = 0
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)
        for item in my_list:
            if item[13].upper() == s_request.upper():
                print(item)
                result += 1
        if result == 0:
            print(f"No such {s_request} procceses")

        csv_file.close()
    contin = input("Enter any symbol to continue:\n")
    return 0
def search_by_phone():
    s_request = input("Enter phone number you want to find: ")
    result = 0
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)
        for item in my_list:
            if item[3] == s_request:
                print(item)
                result += 1
        if result == 0:
            print(f"No such {s_request} phone number")

        csv_file.close()
    contin = input("Enter any symbol to continue:\n")
    return 0

def search_by_destination():
    s_request = input("Enter destination you want to find: ")
    result = 0
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)
        for item in my_list:
            if item[8] == s_request:
                print(item)
                result += 1
        if result == 0:
            print(f"No orders with {s_request} destination!")

        csv_file.close()
    contin = input("Enter any symbol to continue:\n")
    return 0

def search_by_date():
    s_request = input("Enter date of order you want to find: ")
    result = 0
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)
        for item in my_list:
            if item[1] == s_request:
                print(item)
                result += 1
        if result == 0:
            print(f"No orders in {s_request}!")

        csv_file.close()
    contin = input("Enter any symbol to continue:\n")
    return 0
            