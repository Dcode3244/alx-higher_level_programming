#!/usr/bin/python3
'''
Displays all cities of a given state from the states table
of the database hbtn_0e_4_usa Safe from SQL injections.
'''
import sys
import MySQLdb

if __name__ == "__main__":
    name, passwd, db, search = sys.argv[1], sys.argv[2],\
            sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(user=name, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
