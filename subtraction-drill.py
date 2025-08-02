#!/usr/bin/python3

# subtraction drill
# Copyright 2025, Ted Felix
# License: GPL3+

import os
import time
import datetime
import random

# Handle input of integers without crashing.
def input_number2(prompt = ""):
    done = False
    while not done:
        try:
            result = int(input(prompt))
            done = True
        except ValueError:
            # Try again.
            pass
    return result

# Seed the RNG.
random.seed()

# Use a list to reduce the probability of picking 0 and 1.
numbers = [ 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9 ]

# Works for Linux.  "cls" for Windoze.
os.system("clear")

print("Subtraction Facts")
print()

total = input_number2("How many questions? ")

os.system("clear")

# Write to a log file.
file = open("mathlog.txt", "a")
print(file = file)
print("****************************************", file = file)
print("subtraction-drill.py", file = file)
print(datetime.datetime.now(), file = file)

correct = 0
start_time = int(time.time())

for i in range(1, total + 1):
    x = numbers[random.randrange(len(numbers))]
    y = numbers[random.randrange(len(numbers))]
    sum2 = x + y
    question = "<{}>  {} - {} = ".format(i, sum2, x)

    answer = input_number2(question)

    if answer == y:
        print("Correct!")
        correct += 1
    else:
        print()
        print("**************")
        print("*** No, it's", y)
        print(sum2, "-" , x, "?= ", answer, file = file)
    print()

stop_time = int(time.time())
seconds2 = stop_time - start_time

result = "You got {} correct out of {}.\n".format(correct, total)
result += "It took you {}.\n".format(str(datetime.timedelta(seconds = seconds2)))

print(result)

print(result, file = file)
file.close()

