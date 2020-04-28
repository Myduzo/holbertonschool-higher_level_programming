#!/usr/bin/python3
x = 122
while x >= 97:
	print("{}".format(chr(x - 32)) if x % 2 != 0 else chr(x), end='')
	x -= 1
