#!/usr/bin/python3
""" takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    uname, passwd, db, search = args[1], args[2], args[3], args[4]
    db = MySQLdb.connect(host="localhost", user=uname, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    for state in cur.fetchall():
        if (search == state[1]):
            print(state)
