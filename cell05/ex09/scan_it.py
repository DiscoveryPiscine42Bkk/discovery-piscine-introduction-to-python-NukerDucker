#!/usr/bin/env python3
import sys
import re

def count_pattern_occurrences(pattern, text):
    regex = r'\b' + re.escape(pattern) + r'\b'
    matches = re.findall(regex, text)
    return len(matches) if matches else 0

def main():
    if len(sys.argv) < 3:
        print("none")
        sys.exit(1)
    
    search_term = sys.argv[1]
    text_to_search = sys.argv[2]
    
    count = count_pattern_occurrences(search_term, text_to_search)
    print(count if count > 0 else "none")

if __name__ == "__main__":
    main()