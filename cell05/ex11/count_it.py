#!/usr/bin/env python3
import sys
def get_parameters():
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    return sys.argv[1:]

def count_parameters():
    parameters = get_parameters()
    count = len(parameters)
    
    print(f"parameters: {count}.")
    
    for param in parameters:
        print(f"{param}: {len(param)}")
        
if __name__ == "__main__":
    count_parameters()