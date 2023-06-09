import string
import random

def pass_gen(size):
    generatePassword = "".join(random.choice(
        string.ascii_letters + string.digits + string.punctuation) 
        for n in range(size))
    
    return generatePassword

def password_gen():
    while True:
        try:
            size = int(input("How many characters must the password be? "))
            password = pass_gen(size)
            return password
        except ValueError:
            print("Error: Please enter a valid integer")

new_password = password_gen()
print(new_password)
