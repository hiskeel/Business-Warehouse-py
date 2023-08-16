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
# def sum_calc():
    
#     with open('orders_db.csv', 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         my_list = list(reader)
        
#         sum_products_price = 0
#         for item in my_list:
#             if item[2] == my_list[4]:
#                 price_col = item[3] * my_list[5]
#                 sum_products_price += price_col
#             if item[2] == my_list[6]:
#                 price_pl = item[3] * my_list[7]
#                 sum_products_price += price_pl
#         csv_file.close()
#         return sum_products_price
    
def Add_order():
   
            
    with open('orders_db.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        date = datetime.datetime.now()
        writer.writerow([int(input("id")),date, input("Enter client name: "), input("Enter client`s phone number: "), input("Enter colums name: "),int(input("Enter colums quantity: ")),input("Enter plates name: "),int(input("Enter plates quantity: ")),input("Enter destination: "),int(input("Enter total sum: ")),int(input("Enter delivery price")),int(input("Enter avance value: ")), input("Will be vygruzka? :"),input("Procces: ") ])
        file.close()

        
        
    return 0