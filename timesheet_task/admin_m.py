import mysql.connector as mysql
# Connecting to the lifechoicesonline database
mydb = mysql.connect(host='localhost', user='root', passwd='1234', database='lifechoicesonline')
cursor = mydb.cursor()

# This is the secret admin menu where the admins can create, delete users and see who else are admins


def admin_menu():  # Function for the admin menu
    # Printing the welcome message for the admin menu
    print("""
        ____________________________________________________________________________________________________
        _______________________________Welcome to Life Choices Coding Academy_______________________________
        _____________________________________________Admin Menu_____________________________________________
        ____________________________________________________________________________________________________
        ______________________________PLEASE REMEMBER THAT THIS MENU IS SECRET______________________________
        ____________________________________________________________________________________________________
        Option 1: Register a new user
        Option 2: Delete a user
        Option 3: List of database admins

        """)
    while 1:
        try:  # Try catch for the users choice validation
            admin_choices = int(input("Please pick an option above between 1-3:   "))  # Takes the input from the user
            if admin_choices == 1:  # If users choice is 2
                try:
                    print("_" * 100, "\n")  # prints _ to neaten cli area
                    print("Option 1: Create a new admin")  # Option 1 for user to choose
                    print("Option 2: Create a new user")  # Option 2 for user to choose
                    print("_" * 100)  # prints _ to neaten cli area
                    admin_second_choice = int(input("Select and option between 1-2: "))  # Takes the input from the user
                    if admin_second_choice == 1:  # if option 1 is chosen
                        add_new_admin = ("INSERT INTO users (full_name, username, password, student_or_lecturer) "
                                         "VALUES (%s, %s, %s, %s)")  # query to insert data into users table
                        add_new_admin_table = ("INSERT INTO admins(full_name, username, password, "
                                               "student_or_lecturer) Values (%s, %s, %s, %s)")  # Query for admins table
                        print("_" * 100, "\n")  # Print _ to neaten cli area
                        full_name = input("Enter your name and/or surname:  ")  # Takes input for user name
                        username = input("Enter your desired username:  ")  # Takes input for users name
                        password = input("Enter your desired password:  ")  # Takes input for password
                        student_or_lecturer = input("Is the user a student or lecturer: ")  # Takes input for type
                        data_new = [(full_name, username, password, student_or_lecturer)]  # Where query will take data
                        cursor.executemany(add_new_admin, data_new)  # Executing the first query and data
                        cursor.executemany(add_new_admin_table, data_new)  # Executing second query and data
                        mydb.commit()  # Committing the data above
                    if admin_second_choice == 2:  # IF second chose is chosen
                        add_new_admin = ("INSERT INTO users (full_name, username, password, student_or_lecturer) "
                                         "VALUES (%s, %s, %s, %s)")  # Query to insert data into users
                        print("_" * 100, "\n")  # Printing _ to neaten cli
                        full_name = input("Enter your name and or surname:  ")  # Takes input for name
                        username = input("Enter your desired username:  ")  # Takes input for username
                        password = input("Enter your desired password:  ")  # Takes input for password
                        student_or_lecturer = input("Is the user a student or lecturer: ")  # Input for type
                        data_new = [(full_name, username, password, student_or_lecturer)]  # Data set for inputs
                        cursor.executemany(add_new_admin, data_new)  # Executing query
                        mydb.commit()  # Committing the data above
                except ValueError:  # Ensures that a number is entered
                    print("\n Please enter a number between 1-3:    ")  # Error message which prints
                else:
                    if admin_second_choice > 4:
                        print("\n Please enter a number between 1-3:    ")
            elif admin_choices == 2:  # If second choice is chosen
                print("\n", "_"*100)  # Printing _ to neaten cli
                admin_delete = input("Please enter the correct username you wish to delete:\n")  # Takes option input
                admin_sql_delete = ("DELETE FROM users WHERE username ='"+admin_delete+"'")  # Query for user delete
                cursor.execute(admin_sql_delete)  # Executing the query
                mydb.commit()  # Committing the data above
            elif admin_choices == 3:  # If option 3 is chosen
                admin_list = "SELECT * FROM admins"  # Query to print data in admins
                cursor.execute(admin_list)  # Executing the query
                admin_result = cursor.fetchall()  # Fetching all the information
                print("_" * 100)  # Printing _ to neaten cli
                print("The order is:")  # Printing message
                print("'Name', 'Username', 'Password', 'Student or Lecturer'")  # Showing the order of data
                print("_" * 100)  # Printing _ to neaten cli
                for x in admin_result:  # For loop to sift through admins table for x amount of rows
                    print(x)  # Prints info in the table
                mydb.commit()  # Commits the data above
                break
        except ValueError:  # Ensures that a number is entered
            print("\n!!!!!Invalid option!!!!!")  # Error message which prints
        else:
            print("\n")  # Skips a line
            break

    if mydb.is_connected():  # If statement to check if connection between python and mysql is still live
        cursor.close()  # Closes connection
        mydb.close()  # Closes connection
        print("_"*100)  # Prints _ to neaten cli
        print("MySQL connection is closed")  # Message to show that the connection is terminated
        print("THANK YOU !!!")  # Thank you message
