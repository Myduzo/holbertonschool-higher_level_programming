#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number

if number < 0:
    n *= -1

last_digit = n % 10

if last_digit > 5:
	print("Last digit of {:d} is {:d} and is greater than 5 and not 0".format(number, last_digit))
elif last_digit < 6:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_digit))
else:
	print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))