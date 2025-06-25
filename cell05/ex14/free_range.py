#!/usr/bin/env python3
import sys

def get_parameters():
    if len(sys.argv) != 3:
        print("none")
        sys.exit(1)
    return sys.argv[1:]

def free_range():
    parameters = get_parameters()
    
    numbers = []
    first_param = int(parameters[0])
    second_param = int(parameters[1])
    
    for num in range(first_param, second_param + 1):
        numbers.append(num)
    return numbers

def main():
    numbers = free_range()
    
    if not numbers:
        print("none")
    else:
        print(numbers)

if __name__ == "__main__":
    main()
