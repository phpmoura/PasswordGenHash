from passwordGen import pass_gen
from hashpassword import passwordToHash

def password_gen():
    while True:
        try:
            size = int(input("How many characters must the password be? "))
            password = pass_gen(size)
            return password
        except ValueError:
            print("Error: Please enter a valid integer")

my_password = password_gen
my_hash = passwordToHash(my_password)
print(my_hash)
