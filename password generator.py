import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "❌ No character set selected. Please enable at least one option."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
def password_generator():
    print("===== PASSWORD GENERATOR =====")
    
    try:
        length = int(input("Enter desired password length: "))

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits    = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols   = input("Include symbols? (e.g., @#$%) (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"\n🔐 Generated Password: {password}")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number for length.")

# Run the password generator
password_generator()
