#!/usr/bin/python3
"""My Filter States"""


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
    cur.execute("SELECT * FROM states WHERE name = '{}' \
        ORDER BY id".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        if argv[4] == state[1]:
            print(state)
    cur.close()
    db.close()
