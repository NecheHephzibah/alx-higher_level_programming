#!/usr/bin/python3
# Script that lists all cities of a state from the database hbtn_0e_4_usa.

import sys
import MySQLdb

def main():
    # Retrieve argument from the databases
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create the SQL query
    query = """
    SELECT cities.id, cities.name 
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the SQL query with the user input safely
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    cities = [row[1] for row in rows]
    print(", ".join(cities))

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

