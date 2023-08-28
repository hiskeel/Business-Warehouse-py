from func import *
from orders_func import *
from search_func import *

exit_program = False
back = False

while (exit_program != True):
    back = False
    try:
        choice = main_menu()
        if choice == '1':
            while(back != True):
                choice = warehouse_menu()
                if choice == '1':
                    try:
                        show_products()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as err:
                        cont = input(f"file Open error: {error=}, {type(error)=}\nEnter any symbol to continue: ")
                elif choice == '2':
                    try:
                        sort_by_group()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as err:
                        print(f"Unexcepted error: {error=}, {type(error)=}")
                elif choice == '3':
                    try:
                        Sort_products_by_price()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as error:
                        print(f"Unexcepted error: {error=}, {type(error)=}")
                elif choice == '9':
                    back = True
                elif choice == '0':
                    confirmation = input("Are you sure you want to close a program?\n1. Yes\n2. No, stay")
                    if confirmation == '1':
                        print ("Bye!")
                        back = True
                        exit_program = True 
                    elif confirmation == '2':
                        pass
                    else:
                        pass
                else:
                    cont = input("No such menu point\nEnter any symbol to continue: ")
        elif choice == '2':
            back = False
            while(back != True):
                choice = search_menu()
                if choice == '1':
                    try:
                        search_by_name()
                    except Exception as error:
                        cont = input(f"Unexcepted error: {error=}, {type(error)=}\nEnter any symbol to continue: ")

                elif choice == '2':
                    try:
                        search_by_procces()
                    except Exception as error:
                        cont = input(f"Unexcepted error: {error=}, {type(error)=}\nEnter any symbol to continue: ")

                elif choice == '3':
                    try:
                        search_by_phone()
                    except Exception as error:
                        cont = input(f"Unexcepted error: {error=}, {type(error)=}\nEnter any symbol to continue: ")
                elif choice == '4':
                    try:
                        search_by_destination()
                    except Exception as error:
                        cont = input(f"Unexcepted error: {error=}, {type(error)=}\nEnter any symbol to continue: ")
                elif choice == '5':
                    try:
                        search_by_date()
                    except Exception as error:
                        cont = input(f"Unexcepted error: {error=}, {type(error)=}\nEnter any symbol to continue: ")
                elif choice == '9':
                    back = True
                elif choice == '0':
                    confirmation = input("Are you sure you want to close a program?\n1. Yes\n2. No, stay")
                    if confirmation == '1':
                        print ("Bye!")
                        back = True
                        exit_program = True 
                    elif confirmation == '2':
                        pass
                    else:
                        pass
                else:
                    cont = input("No such menu point\nEnter any symbol to continue: ")
        elif choice == '3':
            back = False
            while(back != True):
                choice = product_menu()
                if choice == '1':
                    try:
                        Change_quantity()
                        cont = input("Quantity succesfully edited!\nEnter any symbol to continue: ")
                    except Exception as error:
                        cont = input(f"Unexcepted error: {error=}, {type(error)=}\nEnter any symbol to continue: ")
                elif choice == '2':
                    try:
                        Edit_product()
                        cont = input("Information about product succesfully edited!\nEnter any symbol to continue: ")
                    except Exception as error:
                        print(f"Unexcepted error: {error=}, {type(error)=}")
                elif choice == '3':
                    try:
                        Add_product()
                        cont = input("Product succesfully added!\nEnter any symbol to continue: ")
                    except Exception as error:
                        print(f"Unexcepted error: {error=}, {type(error)=}")
                elif choice == '4':
                    try:
                        Delete_product()
                        cont = input("Product succesfully deleted!\nEnter any symbol to continue: ")
                    except Exception as error:
                        print(f"Unexcepted error: {error=}, {type(error)=}")
                elif choice == '9':
                    back = True
                elif choice == '0':
                    confirmation = input("Are you sure you want to close a program?\n1. Yes\n2. No, stay")
                    if confirmation == '1':
                        print ("Bye!")
                        back = True
                        exit_program = True 
                    elif confirmation == '2':
                        pass
                    else:
                        pass
                else:
                    cont = input("No such menu point\nEnter any symbol to continue: ")
        elif choice == '4':
            back = False
            while(back != True):
                choice = orders_menu()
                if choice == '1':
                    try:
                        Show_orders()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as err:
                        print(f"Unexcepted error: {err=}, {type(err)=}")
                elif choice == '2':
                    try:
                        Add_order()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as err:
                        print(f"Unexcepted error: {err=}, {type(err)=}")
                elif choice =='3':
                    
                    try:
                        Edit_order()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as err:
                        print(f"Unexcepted error: {err=}, {type(err)=}")
                elif choice == '4':
                    try:
                        Delete_order()
                        contin = input("Enter any symbol to continue:\n")
                    except Exception as err:
                        print(f"Unexcepted error: {err=}, {type(err)=}")
                elif choice == '9':
                    back = True
                elif choice == '0':
                    confirmation = input("Are you sure you want to close a program?\n1. Yes\n2. No, stay")
                    if confirmation == '1':
                        print ("Bye!")
                        back = True
                        exit_program = True 
                    elif confirmation == '2':
                        pass
                    else:
                        pass
                else:
                    cont = input("No such menu point\nEnter any symbol to continue: ")
        elif choice == '0':
            confirmation = input("Are you sure you want to close a program?\n1. Yes\n2. No, stay\n")
            if confirmation == '1':
                print ("Bye!")
                exit_program = True 
            elif confirmation == '2':
                pass
            else:
                pass
    except ValueError as err:
        cont = input(f"Value error: {err=}, {type(err)=}\nEnter any symbol to continue: ")
    



