#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}\n".format(value), end="")
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return False
