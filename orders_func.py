import csv
import os
import datetime


id = 1
def Show_orders():
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        temp_list = list(reader)
        i = 1
        while(i < temp_list.__len__()):
            row = temp_list[i]
            print("-----------------------------------------")
            print(f"ID: {row[0]}\nDate: {row[1]}\nClient name: {row[2]}\nPhone number: {row[3]}\nColumn height: {row[4]}\nColumns quantity: {row[5]}\nPlate name: {row[6]}\nPlates quantity: {row[7]}\nDestination: {row[8]}\nTotal sum: {row[9]}\nDelivery price: {row[10]}\nAvance: {row[11]}\nUnloading: {row[12]}\nStatus: {row[13]}\n")
            i +=1
        csv_file.close()
    return 0
def sum_calc(pl_n, col_n, pl_q,col_q):
    sum_products_price = int(0)
    with open('products_DB.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)
        for item in my_list:
            if item[2] ==  col_n:
                price_col = int(item[3]) * col_q
                sum_products_price = sum_products_price + price_col
            if item[2] == pl_n:
                price_pl = int(item[3]) * pl_q
                sum_products_price = sum_products_price + price_pl
        csv_file.close()
    return sum_products_price
    
def Add_order():
    column_name = input("Enter colums name: ")
    col_quantity = int(input("Enter colums quantity: "))
    plates_name = input("Enter plates name: ")
    pl_quantity = int(input("Enter plates quantity: "))
    total_sum = sum_calc(plates_name, column_name, int(pl_quantity),int(col_quantity))
    with open('orders_db.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        curent_datetime = datetime.datetime.now()
        date = curent_datetime.date()
        
        
        writer.writerow([int(input("Enter id: ")),date, input("Enter client name: "), input("Enter client`s phone number: "),column_name, col_quantity, plates_name, pl_quantity,input("Enter destination: "), total_sum,int(input("Enter delivery price")),int(input("Enter avance value: ")), input("Will be unloading? :"),input("Procces: ") ])
        file.close()
    temp_list = []   
    with open('products_DB.csv', 'r') as file:
        reader = csv.reader(file)
        temp_list = list(reader)
        file.close()
    for item in temp_list:
        if item[2] == column_name:
            col_q = int(item[4])
            col_q -= col_quantity
            item[4] = col_q
        if item[2] == plates_name:
            pl_q = int(item[4])
            pl_q -= pl_quantity
            item[4] = pl_q
    with open('products_DB.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(temp_list)
        file.close()
    return 0

def Delete_order():
    Show_orders()
    id = input("Enter id of order you want to DELETE: ")
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = list(reader)

        count = 0
        for row in my_list:
            if row[0] == id:
                my_list.pop(count)
                with open('orders_db.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(my_list)
                    file.close()
            count += 1
        csv_file.close()
    print("Order Succesfully deleted!")
    return 0

def Edit_order():
    choice = input("What do you want to edit:\n1. Edit full order\n2. Edit ordered product information\n3. Edit order status\n4. Edit unloading status\n")
    if choice =='1':
        Show_orders()
        id = input("Enter id of order you want to edit: ")
        with open('orders_db.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            my_list = list(reader)

        # Update the information about the object
            for row in my_list:
                if row[0] == id:
                    column_name = input("Enter colums name: ")
                    col_quantity = int(input("Enter colums quantity: "))
                    plates_name = input("Enter plates name: ")
                    pl_quantity = int(input("Enter plates quantity: "))
                    total_sum = sum_calc(plates_name, column_name, int(pl_quantity),int(col_quantity))
                    row[0] = int(input("Enter new id: "))
                    
                    row[2] = input("Enter new name: ")
                    row[3] = int(input("Enter new phone number: "))
                    row[4] = column_name
                    row[5] = col_quantity
                    row[6] = plates_name
                    row[7] = pl_quantity
                    row[8] = input("Enter new destination: ")
                    row[9] = total_sum
                    row[10] = int(input("Enter new delivery price: "))
                    row[11] = int(input("Enter new avance value: "))
                    row[12] = int(input("Enter new unloading status: "))
                    row[13] = int(input("Enter new status: "))
                    with open('orders_db.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(my_list)
                        file.close()
        csv_file.close()
    elif choice == '2':
        Show_orders()
        id = input("Enter id of product you want to edit: ")
        with open('orders_db.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            my_list = list(reader)

        # Update the information about the object
            for row in my_list:
                if row[0] == id:
                    column_name = input("Enter colums name: ")
                    col_quantity = int(input("Enter colums quantity: "))
                    plates_name = input("Enter plates name: ")
                    pl_quantity = int(input("Enter plates quantity: "))
                    total_sum = sum_calc(plates_name, column_name, int(pl_quantity),int(col_quantity))
                    row[4] = column_name
                    row[5] = col_quantity
                    row[6] = plates_name
                    row[7] = pl_quantity
                    row[9] = total_sum
                    with open('orders_db.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(my_list)
                        file.close()
        csv_file.close()
    elif choice == '3':
        Show_orders()
        id = input("Enter id of product which status you want to edit: ")
        with open('orders_db.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            my_list = list(reader)

        # Update the information about the object
            for row in my_list:
                if row[0] == id:
                    row[13] = input("Enter new status: ")
                    with open('orders_db.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(my_list)
                        file.close()
        csv_file.close()
    elif choice == '4':
        Show_orders()
        id = input("Enter id of product which unloading status you want to edit: ")
        with open('orders_db.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            my_list = list(reader)

        # Update the information about the object
            for row in my_list:
                if row[0] == id:
                    row[12] = input("Enter new unloading status: ")
                    with open('orders_db.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(my_list)
                        file.close()
        csv_file.close()
    else:
        print("Wrong menu point!")