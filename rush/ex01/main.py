#!/usr/bin/env python3
import sys
from checkmate import checkmate

def read_board_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"
    except:
        return "Unable to read file"

def main():
    if len(sys.argv) < 2:
        print("Error: No input files provided")
        return

    for filename in sys.argv[1:]:
        board_str = read_board_file(filename)
        if isinstance(board_str, str) and board_str.startswith("Error") or board_str in ["File not found", "Permission denied", "Unable to read file"]:
            print(f"Error: {board_str} - {filename}")
        else:
            result = checkmate(board_str)
            print(f"{result}")

if __name__ == "__main__":
    main()