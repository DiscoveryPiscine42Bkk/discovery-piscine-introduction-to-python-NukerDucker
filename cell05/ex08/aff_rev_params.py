#!/usr/bin/env python3
import sys

if (len(sys.argv) - 1) < 2:
    print("none")
else:
    reversed_params = sys.argv[1:][::-1]
    for param in reversed_params:
        print(f"{param}")
