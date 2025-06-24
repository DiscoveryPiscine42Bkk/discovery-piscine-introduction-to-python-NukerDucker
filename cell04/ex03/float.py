#!/usr/bin/env python3
user_input = float(input("Give me a number: "))
if user_input - int(user_input) == 0:
    print("This is an integer.")
else:
    print("This is a decimal.")
    