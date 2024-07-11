#Password Generator which is created by using Python Programming.
#This password generator generates random password according to the desired length provided by the user.
#It uses lowercases,uppercases,digits and special characters to generate password.

import random
import string

pass_length = int(input("Enter the desired length for your password:"))        

string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.digits
'0123456789'

string.punctuation
'!@#$%^&*()_-+={}[\\]:;<>?/~`'

characters= string.ascii_letters + string.digits + string.punctuation

password= ""
for index in range(pass_length):
    password= password + random.choice(characters)

print("Password Generated: {}".format(password) )