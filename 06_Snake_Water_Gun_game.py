'''
Snake Water Gun Game

The person that plays the strongest “object” is the winner of the game.Here we have user who
will choose any one object from Snake ,water or gun .Water will win from gun , 
gun will win from snake, snake will win from water.
'''

import random

game_obj = ['snake', 'water', 'gun']


comp, user = 0,0
i = 1

while i<11:

    computer = random.choice(game_obj)
    user_choice = input('Enter you choice: \n1. Snake \n2. Water \n3. Gun\n')


    if computer == "water" and user_choice == "3":
        print("Computer Win this round")
        comp = comp + 1
    elif computer == 'gun' and user_choice == '1':
        print("Computer Win this round")
        comp = comp + 1
    elif computer == 'snake' and user_choice == '2':
        print("Computer Win this round")
        comp = comp + 1
    
    elif computer == "2" or computer == "3" or computer == "1":
        print("Tie")
    else:
        user = user + 1
        print("User Win this round")

    i = i + 1


if user == comp:
    print("Game Tie")

else:
    print("User Wins this game") if user > comp else print("Computer Wins this game")
