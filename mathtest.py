#!/usr/bin/python3

# MATHTEST.BAS ported to python.
# Copyright 2025, Ted Felix
# License: GPL3+

# This only does subtraction with positive numbers.
# Probably need to develop an entire suite covering all the variations.

import os
import time
import datetime
import random

# Seed the RNG.
random.seed()

# Works for Linux.  "cls" for Windoze.
os.system("clear")

print("Timed test.  Ew!")
print()
a = input("Press enter to begin...")

os.system("clear")

total = 100
correct = 0
start_time = int(time.time())

for i in range(1, total + 1):
    x = random.randrange(10)
    y = random.randrange(10)
    sum2 = x + y
    print("<", i, ">  ", sum2, "-", x, "= ", end="")
    answer = int(input())
    if answer == y:
        print("Correct!")
        correct = correct + 1
    else:
        print("No, it's", y)
    print()

stop_time = int(time.time())
seconds2 = stop_time - start_time

result = "You got {} correct out of {}.\n".format(correct, total)
result += "It took you {}.\n".format(str(datetime.timedelta(seconds = seconds2)))

print(result)

# Write to a log file as well.

file = open("mathlog.txt", "a")
print(file = file)
print("****************************************", file = file)
print(datetime.datetime.now(), file = file)
print(result, file = file)
file.close()

