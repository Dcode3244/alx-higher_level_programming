#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_0_usa
- Your script should take 3 arguments:
mysql username, mysql password and database name
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server
running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    uname, passwd, db = args[1], args[2], args[3]
    db = MySQLdb.connect(host="localhost", user=uname, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states
                ON cities.state_id=states.id
                ORDER BY cities.id')
    for s in cur.fetchall():
        print(s)
