import string
import random

def password_g(length):
    if length<4:
        return "Password should be at least 4 characters long"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password=[
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password+=random.choices(characters,k=length-4)
    random.shuffle(password)
    return ''.join(password)
try:
    length=int(input("enter the length of the password: "))
    print(password_g(length))
except ValueError:
    print("Invalid input")