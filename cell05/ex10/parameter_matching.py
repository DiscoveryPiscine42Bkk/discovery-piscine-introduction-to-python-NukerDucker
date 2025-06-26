import sys
def check_parameters():
    if len(sys.argv) != 2:
        print("none")
        sys.exit(1)

def main():
    check_parameters()
    first_param = sys.argv[1]
    
    user_input = input("What was the parameter? ")
    
    if first_param == user_input:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()