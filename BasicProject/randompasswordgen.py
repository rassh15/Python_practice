"""
To generate random password we assign all alphanumeric characters to variable.
And use random module to select character from it.
"""

import random
passlen = int(input("Enter the length of password: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ''
for i in range(passlen):
    password = password + random.choice(s)
#inplace of choice you can use random.sample() 
#which return list of characted of specified length

print(f'Password generated of length {passlen} is {password}')