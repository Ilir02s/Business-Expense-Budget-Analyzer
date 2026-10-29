def user_choice1():
    input("Please add a business expense: ")

def option_2():
    input("Please add a business expense: ")

def option_3():
    input("Please add a business expense: ")

def option_4():
    input("Please add a business expense: ")


def main_menu():
    while True:
        print("\n--Welcome to your personal Business Expense & Budget Analyzer--\n")
        print("1. Add business expense. ")
        print("2. Update existing business expense. ")
        print("3. Delete existing business expense. ")
        print("4. Overview. ")
        user_choice = input("\nPlease choose an option from above: ")
            
        if user_choice == "1":
            input("Please add a business expense: ")
        elif user_choice == "2":
            input("Update your existing business expense: ")
        elif user_choice == "3":
            input("Delete your exisiting business expense: ")
        elif user_choice == "4":
            print("Here is your overview: ")
        elif user_choice not in ("1", "2", "3", "4"):
            print("Please insert a valid choice.")
            break
        else:
            print("Bye.")


if __name__ == "__main__":
    main_menu()