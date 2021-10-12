'''
Program to take input from the user and return meaning of the word
'''

word_dict = {'Table':34, 'Chair':50, 'Utensil': 39,'Bottle':59,'Stool':32}

while True:

    choice = input("Enter the name of the item you want or No: ")

    try:
        if choice=='No':    break
        else:   print(f"\nTotal number of available {choice} is {word_dict[choice]}")
    
    except Exception as e:
        print(f"{choice} not available")
        continue
