import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-zA-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # Special characters

    if not characters:
        print("Error: No character types selected!")
        return ""

    # Randomly select characters from the chosen set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be a positive number!")
            return

        print("\nInclude in password:")
        include_letters = input("Letters (y/n)? ").strip().lower() == 'y'
        include_digits = input("Digits (y/n)? ").strip().lower() == 'y'
        include_symbols = input("Symbols (y/n)? ").strip().lower() == 'y'

        password = generate_password(length, include_letters, include_digits, include_symbols)
        if password:
            print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
