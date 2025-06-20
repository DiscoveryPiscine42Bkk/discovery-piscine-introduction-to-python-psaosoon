def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Welcome, {name}!")
    else:
        print("Error: Name must be a string.")


if __name__ == "__main__":
    greetings()              
    greetings("Alice")       
    greetings(123)     
