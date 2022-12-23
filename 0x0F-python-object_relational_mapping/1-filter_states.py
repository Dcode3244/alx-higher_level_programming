#!/usr/bin/python3
""" lists all states with a name starting with N from
the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE BINARY name LIKE "N%"')
    states = cur.fetchall()

    [print(state) for state in states]
