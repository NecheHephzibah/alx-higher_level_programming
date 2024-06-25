#!/usr/bin/python3
"""
Module that connects to a MySQL database takes in arguent and displays all
values in the states table where name matches the argument.
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
