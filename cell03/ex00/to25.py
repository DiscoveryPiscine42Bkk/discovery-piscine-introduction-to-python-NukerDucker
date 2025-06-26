#!/usr/bin/env python3
input_number = int(input("Enter a number less than 25: "))
if input_number > 25:
    print("Error")
while input_number <= 25:
    print(f"Inside the loop, my variable is {input_number}")
    input_number += 1
