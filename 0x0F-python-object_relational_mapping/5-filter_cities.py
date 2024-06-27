#!/usr/bin/python3
# Script that lists all cities of a state from the database hbtn_0e_4_usa.


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
    cursor.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argv[4], ))
    print(", ".join(map(lambda x: x[0], cursor.fetchall())))
    # Close the cursor and the connection
    cursor.close()
    db.close()
