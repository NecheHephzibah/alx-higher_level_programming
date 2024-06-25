#!/usr/bin/python3
"""
Module that connects to a MySQL database takes in arguent and displays all
values in the states table where name matches the argument.
"""


import sys
import MySQLdb


def main():
    """
    Main function that connects to the MySQL database, and displays all
    values in the states table where name matches the argument.
    """
    # Retrieve arguments from the already created database
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Create the SQL query using parameterized query
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the SQL query with the user input safely
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

