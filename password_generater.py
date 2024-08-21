import random
import string

def password_generator():
    print("Password Generator")
    print("------------------")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        complexity = input("Do you want a simple (only letters), medium (letters and numbers), or complex (letters, numbers, and special characters) password? (simple/medium/complex): ").lower()
        if complexity in ["simple", "medium", "complex"]:
            break
        else:
            print("Invalid input. Please enter 'simple', 'medium', or 'complex'.")
    if complexity == "simple":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()