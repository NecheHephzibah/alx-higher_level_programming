#!/usr/bin/python3
"""Filters states by User Input"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    request = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    request = request.format(argv[4])
    cur.execute(request)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
