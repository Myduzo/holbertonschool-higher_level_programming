#!/usr/bin/python3
"""Filter cities"""


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
    cur.execute("SELECT cities.name \
                FROM cities LEFT JOIN states \
                ON cities.state_id=states.id \
                WHERE states.name=%s \
                ORDER BY cities.id",
                (argv[4],))
    cities = cur.fetchall()
    cities = [city[0] for city in cities]
    print(", ".join(cities))

    cur.close()
    db.close()
