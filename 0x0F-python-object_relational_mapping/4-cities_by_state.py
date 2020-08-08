#!/usr/bin/python3
"""Cities by state"""


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
    cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities, states WHERE states.id = cities.state_id ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
