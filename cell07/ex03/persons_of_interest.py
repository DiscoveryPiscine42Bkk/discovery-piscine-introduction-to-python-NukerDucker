#!/usr/bin/env python3
def famous_births(scientists):
    return dict(sorted(scientists.items(), key=lambda item: item[1]["date_of_birth"]))

def main():
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    sorted_scientists = famous_births(women_scientists)
    for scientist in sorted_scientists.values():
        print(f'{scientist["name"]} is a great scientist born in {scientist["date_of_birth"]}.')

if __name__ == "__main__":
    main()