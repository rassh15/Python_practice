
"""To create a Dice we have use random module to generate random numbers."""

import random

#This will print random number between 1 to 6
while True:
    print("1.Dice Roll\n2.Exit ")
    choice = input("Enter your choice: \n")
    if choice=='1':
        print('Number is ',random.randint(1,6),'\n')
    else:   break