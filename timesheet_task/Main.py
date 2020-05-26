from Number_on_campus import campus_check
from admin_m import admin_menu
from login_logout import login, logout


def main_menu():  # Function for the system
    # Printing the welcome message for the program
    print("""
    ____________________________________________________________________________________________________
    _______________________________Welcome to Life Choices Coding Academy_______________________________
    ____________________________________________________________________________________________________
    Option 1: Login for the day
    Option 2: Logout for the day
    Option 3: Number of staff/students on campus
    
    """)

    try:  # Try catch for the users choice validation
        userchoices = int(input("Please pick an option above between 1-3:   "))  # Takes the input from the user
        if userchoices == 1:  # If users choice is 1
            login()  # Calls the login function from login_logout
        if userchoices == 2:  # If users choice is 2
            logout()  # Calls the logout function from login_logout
        if userchoices == 3:  # Calls the campus_check function from number_on_campus
            campus_check()
        if userchoices == 4:  # Admin login menu THIS IS A SECRET OPTION ONLY ADMINS KNOW
            admin_menu()  # Calls the admin_menu function from admin_m
    except ValueError:  # Ensures that a number is entered
        print("\n Please enter a number between 1-3:    ")  # Error message which prints
    else:
        print("\n")  # Skips a line


main_menu()
