#PASSWORD GENERATOR

import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

password_length = 12
print(f"Generated password: {generate_password(password_length)}")
