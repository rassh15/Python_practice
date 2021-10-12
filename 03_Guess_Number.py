'''
Guess the number
Program to create a guess number by taking input from user till they guess correctly
rule:
limit number of guesses (9)
Number of guesses take to finish
Game Over if fails to guess
'''
number_to_guess = 15

guesses = 8
cnt = 1
while guesses > 0:
    

    entered_numb = int(input("enter number to be guess: "))
    if entered_numb == number_to_guess:
        print(f"You Won\nYou guess the number in {cnt} guesses")
    elif entered_numb > number_to_guess:
        print("Please enter smaller number")

    elif guesses == 1:
        print("Game Over")
    else:
        print("Please enter greater number")

    guesses = guesses - 1
    cnt = cnt + 1

