#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig= (number/10)%
print ("The last digit of {:d} is {:d}".format(number,lastdig))
