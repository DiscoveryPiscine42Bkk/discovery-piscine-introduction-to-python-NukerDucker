#!/usr/bin/python
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
result = input1 * input2
equatuion = f"{input1} x {input2} = {result}"
print(equatuion)
if result < 0:
    print("This result is negative.")
elif result > 0:
    print("This result is positive.")
elif result == 0:
    print("This result is both positive and negative.")