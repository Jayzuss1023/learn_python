import random
import string

def generate_pwd(min_len, numbers=True, special_characters=True):

    letters = string.ascii_letters
    digits = string.digits
    char = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += char

    pwd=""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        rand_char = random.choice(characters)
        pwd += rand_char

        if rand_char in digits:
            has_number = True
        elif rand_char in char:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

password = int(input("Enter a min length for your password: "))
numbers = input("Do you want to include numbers (y/n): ").lower() == "y"
special_characters = input("Do you want to include special characters (y/n): ").lower() == "y"
pwd = generate_pwd(password, numbers, special_characters)
print(pwd)