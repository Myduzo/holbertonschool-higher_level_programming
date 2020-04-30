#!/usr/bin/python3
if __name__ == "__main__":
import sys

argc = len(sys.argv)
argv = sys.argv

print("{} ".format(argc - 1) + \
	("argument" if argc == 2 else "arguments") + \
	("." if argc == 1 else ":") + ("\n"), end='')


x = 1
while x < argc:
	print("{}: {}".format(x, argv[x]))
	x += 1
