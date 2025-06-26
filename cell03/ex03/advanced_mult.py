#!/usr/bin/env python3
num1 = 0
num2 = 0
while num1 <= 10:
    print(f"Table de {num1} ", end='')
    while num2 <= 10:
        result = num1 * num2
        print(f"{result} ", end='')
        num2 += 1
    print()
    num1 += 1
    num2 = 0