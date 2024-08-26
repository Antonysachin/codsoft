import random
import string

def create_password(length, include_letters=True, include_numbers=True, include_specials=True):
    characters = ''
    
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_specials:
        characters += string.punctuation

    if not characters:
        return "You need to select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Random Password Generator!")

    try:
        password_length = int(input("How long should your password be? (Minimum 6 characters): "))
        
        if password_length < 6:
            print("Let's make sure it's at least 6 characters long.")
            password_length = 6

        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters like @, #, $? (y/n): ").strip().lower() == 'y'

        if not (use_letters or use_numbers or use_special_chars):
            print("Please select at least one character type.")
            return

        password = create_password(password_length, use_letters, use_numbers, use_special_chars)
        print(f"Your generated password is: {password}")

    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
