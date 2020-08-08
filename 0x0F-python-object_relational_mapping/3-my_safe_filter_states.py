#!/usr/bin/python3
"""My safe filter states"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(name)s \
        ORDER BY id", {'name': argv[4]})
    states = cur.fetchall()
    for state in states:
        if argv[4] == state[1]:
            print(state)

    cur.close()
    db.close()
