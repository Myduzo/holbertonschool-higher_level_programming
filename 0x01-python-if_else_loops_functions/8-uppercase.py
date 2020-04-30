#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        s = ord(str[x]) - 32
        print("{}".format(chr(s)
              if ord(str[x]) in range(97, 122)
              else str[x]), end=("\n" if x == len(str) - 1 else ""))
