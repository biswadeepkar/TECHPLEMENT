
import random
import time

def generate_password(length, has_uppercase, has_digits, has_special_chars):
    password = []
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_chars = '0123456789'
    special_chars = '!@#$%^&*()_-+=.<>{}[]?/'

    chars = lowercase_chars

    if has_uppercase:
        chars += uppercase_chars
    if has_digits:
        chars += digits_chars
    if has_special_chars:
        chars += special_chars

    for _ in range(length):
        password.append(random.choice(chars))

   
    if has_uppercase and not any(c.isupper() for c in password):
        password[random.randint(0, length - 1)] = random.choice(uppercase_chars)
    if has_digits and not any(c.isdigit() for c in password):
        password[random.randint(0, length - 1)] = random.choice(digits_chars)
    if has_special_chars and not any(c in special_chars for c in password):
        password[random.randint(0, length - 1)] = random.choice(special_chars)

    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Random Password Generator")


    length = int(input("Enter password length: "))

    has_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    has_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    has_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, has_uppercase, has_digits, has_special_chars)

    print("Generated Password:", password)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Execution time: {:.2f} seconds".format(time.time() - start_time))