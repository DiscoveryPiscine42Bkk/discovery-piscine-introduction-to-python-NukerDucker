#!/usr/bin/env python3
import sys

try:
    first_param = sys.argv[1]
    print(f"{first_param}")
except IndexError:
    print("none")
    sys.exit(1)