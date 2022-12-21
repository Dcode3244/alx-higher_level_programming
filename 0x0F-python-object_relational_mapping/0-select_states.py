#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    uname, passwd, db = args[1], args[2], args[3]
    db = MySQLdb.connect(host="localhost", user=uname, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    for state in cur.fetchall():
        print(state)
