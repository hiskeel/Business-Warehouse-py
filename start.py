from func import *

exit_program = False
back = False

while (exit_program != True):
    back = False
    choice = main_menu()
    if choice == 1:
        while(back != True):
            choice = warehouse_menu()
            if choice == 1:
                show_products()
                contin = input("Enter any symbol to continue:\n")
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 9:
                back = True
            elif choice == 0:
                back = True
                exit_program = True
    elif choice == 2:
        back = False
        while(back != True):
            choice = search_menu()
            if choice == 1:
                show_products()
                contin = input("Enter any symbol to continue:\n")
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 9:
                back = True
            elif choice == 0:
                back = True
                exit_program = True
    elif choice == 3:
        back = False
        while(back != True):
            choice = product_menu()
            if choice == 1:
                try:
                    Change_quantity()
                    cont = input("Quantity succesfully edited!\nEnter any symbol to continue: ")
                except err as err
            elif choice == 2:
                Edit_product()
                cont = input("Information about product succesfully edited!\nEnter any symbol to continue: ")
            elif choice == 3:
                Add_product()
                cont = input("Product succesfully added!\nEnter any symbol to continue: ")
            elif choice == 4:
                Delete_product()
                cont = input("Product succesfully deleted!\nEnter any symbol to continue: ")
            elif choice == 9:
                back = True
            elif choice == 0:
                back = True
                exit_program = True
    elif choice == 4:
        back = False
        while(back != True):
            choice = product_menu()
            if choice == 1:
                show_products()
                contin = input("Enter any symbol to continue:\n")
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 9:
                back = True
            elif choice == 0:
                back = True
                exit_program = True



