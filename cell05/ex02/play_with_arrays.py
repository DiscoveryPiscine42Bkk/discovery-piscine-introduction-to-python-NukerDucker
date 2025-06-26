#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -12, 2]
result = []

for number in array:
    if number > 5:
        result.append(number + 2)
        
print(f"{array}")
print(f"{result}")
