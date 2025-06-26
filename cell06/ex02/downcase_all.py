#!/usr/bin/env python3
import sys
def check_params():
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    return sys.argv[1:]

def lowercase_it(string):
    return string.lower()

def main():
    for param in check_params():
        print(lowercase_it(param))
    
if __name__ == "__main__":
    main()