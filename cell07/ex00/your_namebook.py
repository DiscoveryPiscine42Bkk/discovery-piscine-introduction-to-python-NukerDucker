#!/usr/bin/env python3
def array_of_names(dict_name):
    names = []
    for key, value in dict_name.items():
        if isinstance(value, str):
            names.append((key).capitalize() + ' ' + value.capitalize())
    return names

def main():
    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }
    names = array_of_names(persons)
    if not names:
        print("none")
    else:
        print(names)

if __name__ == "__main__":
    main()