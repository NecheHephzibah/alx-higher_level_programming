#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_4_usa.

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "JOIN states ON cities.states_id = states.id "
                   "ORDER BY cities.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
