import hashlib
from passwordGen import new_password

def passwordToHash(new_password):
    string_bytes = new_password.encode('UTF-8')
    hash_object = hashlib.sha256()
    hash_object.update(string_bytes)
    return hash_object.hexdigest()


my_password = new_password
my_hash = passwordToHash(my_password)
print(my_hash)
    
