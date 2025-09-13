import random

char = "abcdefghijlompqrstuvwxyz1234567890ABCDEFGSIJKLOIMPQRSTUVWXYZ!@#$%^&*()"

while 1:
    password_len= int(input("how long would you like your password to be?:"))
    password_count = int(input("how many passwords would you like?:"))
    for x in range(0,password_count):
       password = ""
       for x in range(0, password_len):
           password_char = random.choice(char)
           password = password + password_char
       print(password)