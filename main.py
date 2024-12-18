import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters for security.")

    # Define the character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure the password has at least one character from each pool
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    # Fill the rest of the password length with random choices from all pools
    all_characters = lowercase + uppercase + digits
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to randomize the order
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length (minimum 6): "))
    print("Generated Password:", generate_password(password_length))
