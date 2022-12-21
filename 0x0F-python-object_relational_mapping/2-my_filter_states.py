#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    uname, passwd, db, search = args[1], args[2], args[3], args[4]
    db = MySQLdb.connect(host="localhost", user=uname, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE BINARY "{}"\
                ORDER BY id'.format(search))
    for s in cur.fetchall():
        print(s)
