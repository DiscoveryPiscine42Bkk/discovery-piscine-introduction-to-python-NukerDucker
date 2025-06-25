#!/usr/bin/env python3
def find_the_redheads(family_dict):
    redheads = []
    for key, value in family_dict.items():
        if isinstance(value, str) and value.lower() == "red":
            redheads.append(key)
    return redheads

def main():
    dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
    }
    redheads = find_the_redheads(dupont_family)
    if not redheads:
        print("none")
    else:
        print(redheads)

if __name__ == "__main__":
    main()
        
