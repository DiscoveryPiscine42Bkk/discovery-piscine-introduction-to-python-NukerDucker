#!/usr/bin/python
user_input = input("Enter a number: ")
num = 0
while num < 10:
    result = int(user_input) * num
    print(f"{num} x {user_input} = {result}")
    num += 1