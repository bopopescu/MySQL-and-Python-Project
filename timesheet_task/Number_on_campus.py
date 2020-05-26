import mysql.connector as mysql

# Connecting to the lifechoicesonline database

mydb = mysql.connect(host='localhost', user='root', passwd='1234', database='lifechoicesonline')
cursor = mydb.cursor()


# This piece of code is to see how many people are on campus in case a headcount needs to take place
# I achieve this by subtracting the amount of entries in logged_in table by the entries in logged_out table
def campus_check():
    cursor.execute("SELECT COUNT(user_id) FROM logged_in")
    # Executing the first query and data
    rows = cursor.fetchall()
    cursor.execute("SELECT COUNT(user_id) FROM logged_out")
    # Executing the second query and data
    rows_out = cursor.fetchall()
    print(rows, "This is number 1\n")
    print(rows_out, "This is number 2,\nplease subtract number 1 with this number")
    print("After subtracting 2 from 1, The answer is how many people are on campus")
