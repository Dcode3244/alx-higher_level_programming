#!/usr/bin/python3
'''
Displays all cities of a given state from the states table
of the database hbtn_0e_4_usa Safe from SQL injections.
'''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute('SELECT * FROM cities INNER JOIN states\
                ON states.id=cities.state_id\
                ORDER BY cities.id')

    cities = cur.fetchall()
    filtered_city = ", ".join(city[2] for city in cities if city[4] == argv[4])

    print(filtered_city)
