import random

char = "abcdefghijlompqrstuvwxyz1234567890ABCDEFGSIJKLOIMPQRSTUVWXYZ!@#$%^&*()"

def get_password_len():
    while True:
        try:
            return int(input("how long would you like your password to be?:"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_password_count():
    while True:
        try:
            return int(input("how many passwords would you like?:"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while 1:
    password_len= get_password_len()
    password_count = get_password_count()
    for x in range(0,password_count):
       password = ""
       for x in range(0, password_len):
           password_char = random.choice(char)
           password = password + password_char
       print(password)
