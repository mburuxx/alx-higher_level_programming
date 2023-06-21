#!/usr/bin/python3
"""Script that takes in arguments and displays all
values but is safe from MySQL injections.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(rows)
