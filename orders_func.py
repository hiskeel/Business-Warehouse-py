import csv
import os
import datetime

id = 1
def Show_orders():
    with open('orders_db.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
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
    choice = input("What do you want to edit:\n1.Edit full order\n2. Edit ordered product information\n3. Edit order status\n4. Edit unloading status\n")
    if choice =='1':
        pass
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