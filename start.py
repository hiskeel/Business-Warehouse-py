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
                show_products()
                contin = input("Enter any symbol to continue:\n")
            elif choice == 2:
                Edit_product()
            elif choice == 3:
                Add_product()
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



