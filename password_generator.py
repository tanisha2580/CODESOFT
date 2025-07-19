# password_generator_cli.py

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    # Combine character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("----- Password Generator -----")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()