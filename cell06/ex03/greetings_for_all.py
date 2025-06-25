#!/usr/bin/env python3

def greetings(name='noble stranger') -> str:
    if not isinstance(name, str):
        return 'Error! It was not a name.'
    return f'Hello, {name}.'

def main() -> None:
    print(greetings('Alexandra'))
    print(greetings('Wil'))
    print(greetings())
    print(greetings(42))

if __name__ == '__main__':
    main()
