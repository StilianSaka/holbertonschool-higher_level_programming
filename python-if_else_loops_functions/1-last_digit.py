#!/usr/bin/python3
import random
text = "Last digit of"
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    print(f"{text} {number} is {last_digit} and is greater than 5")

if last_digit == 0:
    print(f"{text} {number} is {last_digit} and is 0")

if last_digit != 0 and last_digit < 6:
    print(f"{text} {number} is {last_digit} and is less than 6 and not 0")
