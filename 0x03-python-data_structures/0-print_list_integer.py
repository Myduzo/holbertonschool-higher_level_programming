#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = 0
    while x in range(len(my_list)):
        print("{}\n".format(my_list[x]), end="")
        x += 1