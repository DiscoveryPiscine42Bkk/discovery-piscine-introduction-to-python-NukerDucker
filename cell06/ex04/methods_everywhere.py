#!/usr/bin/env python3
import sys
def check_params():
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    return sys.argv[1:]

def shrink(string):
    return string[:8]

def enlarge(string):
    return string + ('Z' * (8 - len(string)))

def main():
    params = check_params()
    
    for param in params:
        if len(param) < 8:
            print(enlarge(param))
        else:
            print(shrink(param))
        
if __name__ == "__main__":
    main()