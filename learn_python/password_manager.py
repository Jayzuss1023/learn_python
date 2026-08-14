from cryptography.fernet import Fernet


# Create a key. This secret_key will be used to encrypt and decrypt the password
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def cipher_key():
    key = load_key()
    cipher_suite = Fernet(key)
    return cipher_suite


def create():
    # Open - method to open a file
    # Args("txt file", "mode: a = append")

    # Method 2: You'll need to manually close the file
    # file = open("passwords.txt", "a") as f
    # file.close()
    # with: closes the file itself
    name = input("Account Name: ")
    pwd = input("Password: ")
    cipherer = cipher_key()
    with open("passwords.txt", "a") as f:
        data = f.write(name + "|" + cipherer.encrypt(pwd.encode("utf-8")).decode() + "\n")
        print(data)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            password = pwd.encode("utf-8")
            cipherer = cipher_key()
            print("USER:", user, "PASSWORD:", cipherer.decrypt(password).decode())

while True:
    mode = input("Would you like to create a new password or view existing ones? Press q to quit: (create/view) ").lower()

    if mode == "q":
        break

    if mode == "create":
        create()
    
    elif mode == "view":
        view()
    
    else:
        print("Invalid selection")
        break