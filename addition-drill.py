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

# Use a list to reduce the probability of picking 0 and 1.
numbers = [ 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9 ]

# Works for Linux.  "cls" for Windoze.
os.system("clear")

print("Addition Facts")
print()

total_string = ""
# How do we check for int?
while not total_string.isdigit():
    total_string = input("How many questions? ")

total = int(total_string)

os.system("clear")

file = open("mathlog.txt", "a")
print(file = file)
print("****************************************", file = file)
print(datetime.datetime.now(), file = file)

correct = 0
start_time = int(time.time())

for i in range(1, total + 1):
    x = numbers[random.randrange(len(numbers))]
    y = numbers[random.randrange(len(numbers))]
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

