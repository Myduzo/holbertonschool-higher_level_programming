#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == "+":
        print("{} + {} = {}\n".format(a, b, add(a, b)), end='')

    elif op == "-":
        print("{} - {} = {}\n".format(a, b, sub(a, b)), end='')

    elif op == "*":
        print("{} * {} = {}\n".format(a, b, mul(a, b)), end='')

    elif op == "/":
        print("{} / {} = {}\n".format(a, b, div(a, b)), end='')

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
