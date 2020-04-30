#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    argv = sys.argv

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)), end='')

    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)), end='')

    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)), end='')

    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)), end='')

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
