import sys

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        user_input = input("Please enter a parameter: ").strip()
        if user_input:
            print(user_input)
        else:
            print("none.")
        

if __name__ == "__main__":
    main()