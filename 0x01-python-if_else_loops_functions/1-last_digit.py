#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Calculate the last digit while considering the sign
last_digit = number % 10

# Print the information about the last digit
message = "Last digit of {} is {} and is".format(number, last_digit)

# Check conditions based on the last digit
if last_digit == 0:
    print(message, "0")
elif last_digit > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")
