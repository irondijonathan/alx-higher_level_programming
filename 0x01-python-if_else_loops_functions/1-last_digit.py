#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
lastd = number % 10
if exe == 1:
    number *= -1
    last_number *= -1
print("Last digit of {:d} is ".format(number), end="")
if last_number > 5:
    print("{:d} and is greater than 5".format(last_number))
elif last_number == 0:
    print("{:d} and is 0".format(last_number))
else:
    print("{:d} and is less than 6 and not 0".format(last_number))
