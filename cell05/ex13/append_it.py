#!/usr/bin/env python3
import sys
def get_parameters():
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    return sys.argv[1:]

def ism_check():
    ism_words = []
    parameters = get_parameters()
    
    for param in parameters:
        if 'ism' not in param:
            ism_words.append(param + 'ism')
            
    return ism_words

def main():
    ism_words = ism_check()
    
    if not ism_words:
        print("none")
    else:
        for word in ism_words:
            print(word)
            
if __name__ == "__main__":
    main()