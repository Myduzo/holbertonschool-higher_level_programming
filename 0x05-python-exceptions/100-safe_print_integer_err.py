#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value), end="")
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return False
    return True
