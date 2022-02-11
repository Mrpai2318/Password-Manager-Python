import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="radheshpai",
    database="passwd",
    auth_plugin='mysql_native_password'
)

print(db)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE passwords(Website varchar(20), Username varchar(30), "
                 "Password varchar(30), Date varchar(10) not null)")

print("You have successfully created your database.")
print("You can now use the password manager.")
print("THANK YOU!")
