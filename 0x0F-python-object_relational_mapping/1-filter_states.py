#!/usr/bin/python3
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
	cur.execute("SELECT * FROM states ORDER BY id")
	states = cur.fetchall()
	for state in states:
		if state[1][0] == "N":
			print(state)

	cur.close()
	db.close()
