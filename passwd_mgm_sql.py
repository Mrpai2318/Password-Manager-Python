import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="radheshpai",
    database="passwd",
    auth_plugin='mysql_native_password'
)

print("PLEASE MAKE SURE THAT YOU HAVE RUN \"setup.py\" BEFORE!!!!!")
print(db)
print("Successfully connected to the database")

mycursor = db.cursor()


def mainmenu():
    print("")
    print("WELCOME TO PASSWORD MANAGER")
    print("MAIN MENU")
    print("1.Enter \"See all\" to show all the passwords.")
    print("2.Enter \"New\" to enter a new password.")
    print("3.Enter \"Delete\" to delete a password.")
    print("4.Enter \"Search\" to search for any password.")
    print("5.Enter \"Reset\" to reset the whole database and to remove all the passwords.")

    print(" ")

    user_input = input("Please enter option from the above given menu: ")
    user_input = user_input.upper()

    if user_input == "SEE ALL":
        see_allpasswds()
    elif user_input == "NEW":
        add_newpasswd()
    elif user_input == "DELETE":
        delete_passwd()
    elif user_input == "SEARCH":
        search()
    elif user_input == "RESET":
        reset_database()
    else:
        print("ERROR: The option you have chosen is incorrect")
        print("Please choose the option from the given menu!!!")
        print(" ")

        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def see_allpasswds():
    print(" ")
    mass_passwd = input("Please enter master password: ")
    if mass_passwd == "radz":
        mycursor.execute("SELECT * FROM passwords")
        results = mycursor.fetchall()
        print(tabulate(results, headers=['Website', 'Username/Email_ID', 'Password', 'Date'], tablefmt='fancy_grid'))

        print("All the data in the database.")
        print(" ")

        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()
    else:
        print("ERROR:Wrong input program rerun")
        menu



def add_newpasswd():
    print("  ")

    print("Add data accordingly as given.")
    websites = input("Enter Website: ")
    usernames = input("Enter Username or an Email_Id: ")
    passwords = input("Enter the password: ")
    dates = input("Enter the date when password created/uploaded in yyyy/mm/dd format: ")

    sql = "INSERT INTO passwords (Website, Username, Password, Date) VALUES (%s, %s, %s, %s)"
    value = (websites, usernames, passwords, dates)

    mycursor.execute(sql, value)
    db.commit()

    print("Your password has been inserted into the database!!!")

    print(" ")

    print("Do you want to enter more passwords? ")
    print("Enter \"YES\" if you want to add.")
    print("Enter \"NO\" to go back to mainmenu.")
    userInput = input("Enter option: ").upper()
    if userInput == "YES":
        add_newpasswd()
    elif userInput == "NO":
        menu()
    else:
        print("ERROR:Wrong Input")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def delete_passwd():
    print("So you want to delete a password?")

    userInput = input("Enter \"YES\" OR \"NO\": ")
    userInput = userInput.upper()

    if userInput == "YES":
        delete = input("Enter the website you want to delete the password for: ")
        sql = "DELETE FROM passwords WHERE website = %s"
        val = (delete,)
        mycursor.execute(sql, val)
        db.commit()
        print("The data saved in the website you choose has been deleted from database.")
        print(" ")
        print("Do you want to delete again? ")
        print("Enter \"YES\" to delete again.")
        print("Enter \"NO\" to go back to the mainmenu")
        user_input = input("Enter option: ").upper()
        if user_input == "YES":
            delete_passwd()
        elif user_input == "NO":
            menu()
        else:
            print("ERROR:Wrong Input")
            print("Enter \"Back\" to go back to the menu.")
            userInput = input("Enter option: ").upper()
            if userInput == "BACK":
                menu()
            else:
                print("ERROR:Wrong input program rerun")
                menu()

    elif userInput == "NO":
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()

    else:
        print("Error:Wrong Input")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def search():
    print(" ")
    print("You can now choose how you want to search the database")
    print("Enter \"Website\" if you want to search for a website")
    print("Enter \"Username\" if you want to search for a username")
    print("Enter \"Password\" if you want to search for a password")

    searchInput = input("Enter your option: ").upper()

    if searchInput == "WEBSITE":
        website_search()
    elif searchInput == "USERNAME":
        username_search()
    elif searchInput == "PASSWORD":
        passwd_search()
    else:
        print("ERROR:Wrong Input")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def website_search():
    print("You have choose to search the database using website name.")

    searchWebsite = input("Enter website: ")

    sql = "SELECT * FROM passwords WHERE Website = %s"
    val = (searchWebsite,)
    mycursor.execute(sql, val)
    sresult = mycursor.fetchall()
    for x in sresult:
        print(x)
    print(" ")

    print("Do you want to search database again.")
    print("Enter \"YES\" to search again.")
    print("Enter \"NO\" to go back to the menu")
    userInput = input("Enter option: ").upper()
    if userInput == "YES":
        search()
    elif userInput == "NO":
        menu()
    else:
        print("ERROR:Wrong Input")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def username_search():
    print("You have choose to search the database using username.")

    searchUsername = input("Enter Username: ")

    sql = "SELECT * FROM passwords WHERE Username = %s"
    val = (searchUsername,)
    mycursor.execute(sql, val)
    sresult = mycursor.fetchall()
    for x in sresult:
        print(x)
    print(" ")

    print("Do you want to search database again.")
    print("Enter \"YES\" to search again.")
    print("Enter \"NO\" to go back to the menu")
    userInput = input("Enter option: ").upper()
    if userInput == "YES":
        search()
    elif userInput == "NO":
        menu()
    else:
        print("ERROR:Wrong Input")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def passwd_search():
    print("You have choose to search the database using password.")

    searchPasswd = input("Enter Password: ")

    sql = "SELECT * FROM passwords WHERE Password = %s"
    val = (searchPasswd,)
    mycursor.execute(sql, val)
    sresult = mycursor.fetchall()
    for x in sresult:
        print(x)
    print(" ")

    print("Do you want to search database again.")
    print("Enter \"YES\" to search again.")
    print("Enter \"NO\" to go back to the menu")
    userInput = input("Enter option: ").upper()
    if userInput == "YES":
        search()
    elif userInput == "NO":
        menu()
    else:
        print("ERROR:Wrong Input")
        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


def reset_database():
    print("Enter \"RESET\" if you want to reset database.")
    print("Enter \"Back\" if you want to go back to menu.")

    reset = input("Enter Option: ").upper()
    if reset == "RESET":
        database_reset()
    elif reset == "BACK":
        menu()
    else:
        print("ERROR:Wrong Input")
        reset_database()


def database_reset():
    mycursor.execute("DELETE FROM passwords")
    db.commit()

    print("Your database has been completely erased.")

    print(" ")

    print("Enter \"Back\" to go back to the menu.")
    userInput = input("Enter option: ").upper()
    if userInput == "BACK":
        menu()
    else:
        print("ERROR:Wrong input program rerun")
        menu()


def app_exit():
    print("Thank You for using password manager!")
    print("BYE SEE YOU SOON")


def menu():
    print(" ")
    print("MAIN MENU:")
    print("Enter \"See all\" to show all the passwords.")
    print("Enter \"New\" to enter a new password.")
    print("Enter \"Delete\" to delete a password.")
    print("Enter \"Search\" to search for any password.")
    print("Enter \"Reset\" to reset the whole database and to remove all the passwords.")
    print("Enter \"Exit\" to exit the application.")
    print(" ")

    user_input = input("Please enter option from the above given menu: ")
    user_input = user_input.upper()

    if user_input == "SEE ALL":
        see_allpasswds()
    elif user_input == "NEW":
        add_newpasswd()
    elif user_input == "DELETE":
        delete_passwd()
    elif user_input == "SEARCH":
        search()
    elif user_input == "RESET":
        reset_database()
    elif user_input == "EXIT":
        app_exit()
    else:
        print("ERROR: The option you have chosen is incorrect")
        print("Please choose the option from the given menu!!!")
        print(" ")

        print("Enter \"Back\" to go back to the menu.")
        userInput = input("Enter option: ").upper()
        if userInput == "BACK":
            menu()
        else:
            print("ERROR:Wrong input program rerun")
            menu()


mainmenu()
