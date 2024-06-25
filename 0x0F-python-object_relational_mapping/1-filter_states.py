#!/usr/bin/python3
"""Module that connects to a MySQL database and lists all states starting"""

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

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name
                   LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
