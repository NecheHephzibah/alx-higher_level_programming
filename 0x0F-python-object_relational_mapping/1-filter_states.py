#!/usr/bin/python3
"""
Module that connects to a MySQL database and lists all states starting
with N from the states table.
"""


import sys
import MySQLdb


def main():
    """
    Main function that connects to the MySQL database, and lists all states
    starting with 'N' from the states table, and prints them.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name
                   LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
