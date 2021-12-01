'''
Generate a random interger from a to b.You and your friend to guess a number between two numbers
a and b. a and b are inputs taken from the user.
Your friend is player 1 and plays first. He will have to
keep choosing the number and your program must tell whether
the number is greate than the actual number or less than
the actual number. Log the number of trials it took
you friend to arrive at the number. You play the same game and 
then the person with minimum number of trails wins.
'''

import random

print("Please enter range for A and B: ")
a = int(input('A: '))
b = int(input('B: '))

number = 0
game_score = {"player_1" : 0, "player_2" : 0}

for i in range(1,3):
    tries = 0  
    print(f"\nPlayer {i}")      
    number = random.randint(a,b)
    while True:
        guess = int(input("Guess the number: "))
        tries = tries + 1
        if guess == number:
            print(f"You guess the number in {tries} tries")
            game_score["player_"+str(i)] = tries
            game_score['number'+str(i)] = number

            break
        elif guess > number:
            print("Please enter smaller number ")
        else: print("Please enter larger number ")

print(game_score)
if game_score["player_1"] > game_score["player_2"]: 
    print('Player 2 WINs')
else: print('Player 1 WINs')




