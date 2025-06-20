def main():
    user_input = input("Please enter some parameters (separate by space): ")

    params = user_input.split()
    num_params = len(params)
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()