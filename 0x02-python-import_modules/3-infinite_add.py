#!/usr/bin/python3
if __name__ == "__main__":
	import sys

	argc = len(sys.argv)
	argv = sys.argv
	result = 0

	if (argc == 1):
		print(result)

	if (argc > 1):
		x = 1
		while x < argc:
			result += int(argv[x])
			x += 1
		print(result)
