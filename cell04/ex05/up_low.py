#!/usr/bin/env python3
user_input = input()
result = ""
for char in user_input:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(result)