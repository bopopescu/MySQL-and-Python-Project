import datetime

import mysql.connector as mysql

# Connecting to the lifechoicesonline database
mydb = mysql.connect(host='localhost', user='root', passwd='1234', database='lifechoicesonline')
cursor = mydb.cursor()


# This is the code for the login and out section of the menu
def login():
    print("Welcome to the login screen!")
    print("_" * 100)  # Prints _ to neaten cli
    login_username = input("Please enter your user ID:  ")  # Takes input from user
    user_password = input("Please enter your password:  ")  # Takes input from user
    login_time = datetime.datetime.now()  # Gets the time at the moment of entry
    login_query = "INSERT INTO logged_in(user_id, password, time_in) VALUES (%s, %s, %s)"  # Command to query
    data_new_login = [(login_username, user_password, login_time)]  # Storing data to be queried
    cursor.executemany(login_query, data_new_login)  # Executing the first query and data
    mydb.commit()  # Committing the data above
    if mydb.is_connected():  # If statement to check if connection between python and mysql is still live
        cursor.close()  # Closes connection
        mydb.close()  # Closes connection
        print("_" * 100)  # Prints _ to neaten cli
        print("MySQL connection is closed")  # Message to show that the connection is terminated
        print("THANK YOU !!!")  # Thank you message


def logout():
    print("Welcome to the logout screen!")
    print("_" * 100)  # Prints _ to neaten cli
    logout_username = input("Please enter your user ID:  ")  # Takes input from user
    user_password = input("Please enter your password:  ")  # Takes input from user
    logout_time = datetime.datetime.now()  # Gets the time at the moment of entry
    logout_query = "INSERT INTO logged_out(user_id, password, time_out) VALUES (%s, %s, %s)"  # Command to query
    data_new_logout = [(logout_username, user_password, logout_time)]  # Storing data to be queried
    cursor.executemany(logout_query, data_new_logout)  # Executing the first query and data
    mydb.commit()  # Committing the data above
    if mydb.is_connected():  # If statement to check if connection between python and mysql is still live
        cursor.close()  # Closes connection
        mydb.close()  # Closes connection
        print("_" * 100)  # Prints _ to neaten cli
        print("MySQL connection is closed")  # Message to show that the connection is terminated
        print("THANK YOU !!!")  # Thank you message
