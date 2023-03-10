#!/usr/bin/python3
import random
number = random.randint(-100, 100)

n = number % 10
if number < 0:
    print("The last digit of {} is {}".format(number, (n - 10)))
else:
    print("The last digit of {} is {}".format(number, n))
