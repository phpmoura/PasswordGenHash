import string
import random

def pass_gen(size):
    generatePassword = "".join(random.choice(
        string.ascii_letters + string.digits + string.punctuation) 
        for n in range(size))
    
    return generatePassword

while True:

    try:
        size = int(input("How many characters must the password be? "))
        password = pass_gen(size)
        print(password)
        break
    
    except ValueError:
        print("Error: Please enter a valid integer.")
