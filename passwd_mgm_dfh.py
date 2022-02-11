import random
import pickle
import pyperclip

info_passwd = {}


def mainmenu():
    print(" ")
    print("WELCOME TO PASSWORD GENERATOR AND KEEPER")
    print("MAIN MENU")
    print("1.Enter \"First\" if running for 1st time.")
    print("2.Enter \"Gen Password\" to generate password and store it.")
    print("3.Enter \"Get Password\" to access the stored password")
    print("4.Enter \"Exit\" to exit the program")
    print(" ")

    user_input = input("Please enter values from the above given menu: ")
    user_input = user_input.upper()

    if user_input == "FIRST":
        passwd_gen1st()
    elif user_input == "GEN PASSWORD":
        passwd_gen2nd()
    elif user_input == "GET PASSWORD":
        get_passwd()
    elif user_input == "EXIT":
        passwd_exit()
    else:
        print("ERROR: The option you have chosen is incorrect")
        print("Please choose the option from the given menu!!!")
        print(" ")

        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            mainmenu()
        else:
            print("ERROR:Wrong input program rerun")
            mainmenu()


def passwd_gen2nd():
    with open("passwd.dat", "br") as readfile:
        info_passwd = pickle.load(readfile)

    p = "abcdefghijklmnopqrstuvwxyz012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    len_passwd = int(input("Enter the no of characters in your password: "))

    passwd = "".join(random.sample(p, len_passwd))
    print("Your generated password is: ", passwd)

    ans = input("Do you want to store your password: ").upper()

    if "YES" in ans:
        acc_name = input("Enter name of account you are going use this password for: ")
        info_passwd[acc_name] = passwd

        with open("passwd.pp", "bw") as filewrite:
            pickle.dump(info_passwd, filewrite, protocol=5)

        print("Do you want to enter more passwords?")
        print("Please enter \"Yes\" or \"No\"")
        option = input("ENTER OPTION: ")

        if option.upper() == "YES":
            passwd_gen2nd()
        elif option.upper() == "NO":
            print("Type \"Main Menu\" to go to Main menu")
            print("Type \"Exit\" to exit the program")
            opt = input("ENTER OPTION: ").upper()

            if opt == "MAIN MENU":
                mainmenu()
            elif opt == "EXIT":
                passwd_exit()
            else:
                print("You have entered wrong options")
                print("Program rerun")
                mainmenu()
        else:
            print("Enter \"Back\" to go back to the menu.")
            userInput = input("Enter option: ").upper()
            if userInput == "BACK":
                mainmenu()
            else:
                print("ERROR:Wrong input program rerun")
                mainmenu()

    else:
        print("You didn't want save the password")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            mainmenu()
        else:
            print("ERROR:Wrong input program rerun")
            passwd_gen2nd()


def passwd_gen1st():
    p = "abcdefghijklmnopqrstuvwxyz012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    len_passwd = int(input("Enter the no of characters in your password: "))

    passwd = "".join(random.sample(p, len_passwd))
    print("Your generated password is: ", passwd)

    ans = input("Do you want to keep your password: ").upper()

    if "YES" in ans:
        acc_name = input("Enter name of account you are going use this password for: ")
        info_passwd[acc_name] = passwd

        with open("passwd.pp", "bw") as filewrite:
            pickle.dump(info_passwd, filewrite, protocol=5)

        print("Do you want to enter more passwords?")
        print("Please enter \"Yes\" or \"No\"")
        option = input("ENTER OPTION: ")

        if option.upper() == "YES":
            passwd_gen2nd()
        elif option.upper() == "NO":
            print("Type \"Main Menu\" to go to Main menu")
            print("Type \"Exit\" to exit the program")
            opt = input("ENTER OPTION: ").upper()

            if opt == "MAIN MENU":
                mainmenu()
            elif opt == "EXIT":
                passwd_exit()
            else:
                print("You have entered wrong options")
                print("Program rerun")
                mainmenu()
        else:
            print("Enter \"Back\" to go back to the menu.")
            userInput = input("Enter option: ").upper()
            if userInput == "BACK":
                mainmenu()
            else:
                print("ERROR:Wrong input")
                passwd_gen1st()
    else:
        print("You didn't want save the password")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            mainmenu()
        else:
            print("ERROR:Wrong input program rerun")
            passwd_gen1st()


def get_passwd():
    m_passwd = input("Enter master password: ")

    if m_passwd == "radhu":
        account_name = input("Enter account name: ")
        with open("passwd.pp", "br") as readfile:
            info = pickle.load(readfile)

        if account_name in info:
            pyperclip.copy(info[account_name])
            print("Password Copied")
            print("Enter \"Yes\" to get more passwords")
            print("Enter \"Menu\" to go to menu")
            print("Enter \"Exit\" to exit the program")

            option = input("Enter option from above: ")
            option = option.upper()

            if option == "YES":
                get_passwd2()
            elif option == "MENU":
                mainmenu()
            elif option == "EXIT":
                passwd_exit()
            else:
                print("ERROR:Wrong input program rerun")
                get_passwd2()

        else:
            print("Password not found!!!!")
            print("Enter \"Menu\" to go to menu")
            print("Enter \"Exit\" to exit the program")

            option = input("Enter option from above: ")
            option = option.upper()

            if option == "MENU":
                mainmenu()
            elif option == "EXIT":
                passwd_exit()
            else:
                print("ERROR:Wrong input program rerun")
                get_passwd2()

    else:
        print("Master password wrong")
        get_passwd()


def get_passwd2():
    account_name = input("Enter account name: ")
    with open("passwd.pp", "br") as readfile:
        info = pickle.load(readfile)

    if account_name in info:
        pyperclip.copy(info[account_name])
        print("Password Copied")
        print("Enter \"Yes\" to get more passwords")
        print("Enter \"Menu\" to go to menu")
        print("Enter \"Exit\" to exit the program")

        option = input("Enter option from above: ")
        option = option.upper()

        if option == "YES":
            get_passwd2()
        elif option == "MENU":
            mainmenu()
        elif option == "EXIT":
            passwd_exit()

    else:
        print("Password not found!!!!")
        print("Enter \"Menu\" to go to menu")
        print("Enter \"Exit\" to exit the program")

        option = input("Enter option from above: ")
        option = option.upper()

        if option == "MENU":
            mainmenu()
        elif option == "EXIT":
            passwd_exit()
        else:
            print("ERROR:Wrong input program rerun")
            get_passwd2()


def passwd_exit():
    print("EXITING THE PROGRAM")
    print("Thank You for using Password Manger & Keeper")


mainmenu()
