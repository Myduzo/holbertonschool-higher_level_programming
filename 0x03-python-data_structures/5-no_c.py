#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for x in my_string:
        if not (x == "c" or x == "C"):
            no_c += x

        no_c += ""
    return no_c
