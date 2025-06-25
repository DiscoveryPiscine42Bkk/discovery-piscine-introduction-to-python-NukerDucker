#!/usr/bin/env python3
import sys
def get_parameters():
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    return sys.argv[1:]

def z_finder():
    parameters = get_parameters()
    z_count = 0
    
    for param in parameters:
        z_count += param.count('z')
    
    return z_count

def main():
    z_count = z_finder()
    
    if z_count == 0:
        print("none")
    else:
        print('z' * z_count)
        
if __name__ == "__main__":
    main()