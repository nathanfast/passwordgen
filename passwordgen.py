import string
import random

print ("Passwordmanager made by Fast")
print ("Visit https://github.com/nathanfast")
print ("")

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

password_length = int(input("Enter the desired length of the password: "))
print("Generated Password: ", generate_password(password_length))

