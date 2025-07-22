#!/usr/bin/python3

# addition drill
# Copyright 2025, Ted Felix
# License: GPL3+

import os
import time
import datetime
import random

# Seed the RNG.
random.seed()

# Works for Linux.  "cls" for Windoze.
os.system("clear")

print("Addition Facts")
print()
a = input("Press enter to begin...")

os.system("clear")

file = open("mathlog.txt", "a")
print(file = file)
print("****************************************", file = file)
print(datetime.datetime.now(), file = file)

total = 25
correct = 0
start_time = int(time.time())

for i in range(1, total + 1):
    x = random.randrange(10)
    y = random.randrange(10)
    sum2 = x + y
    print("<", i, ">  ", x, "+", y, "= ", end="")
    answer = int(input())
    if answer == sum2:
        print("Correct!")
        correct = correct + 1
    else:
        print("No, it's", sum2)
        print(x, "+" , y, "?= ", answer, file = file)
    print()

stop_time = int(time.time())
seconds2 = stop_time - start_time

result = "You got {} correct out of {}.\n".format(correct, total)
result += "It took you {}.\n".format(str(datetime.timedelta(seconds = seconds2)))

print(result)

# Write to a log file as well.

print(result, file = file)
file.close()

