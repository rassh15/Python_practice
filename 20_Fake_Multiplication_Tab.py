''''
Rohan das is a fraud by nature
ROhan Das wrote a python function to print a multiplication table
of a given number and put one of the values(randomply genrated) as wrong
Rohan Das did this to fool this classmates and make them commit a mistake
in a test. You cannot tolerate this!. SO you decided to use your
python skills to counter Rohan's actions by writing a python program
that validate Rohan's multiplication Table.
Your function should be able to find out the wrong values in Rohan's Table
and expose Rohan Das as a fraud.
Note: Rohan's function returns a list of number like this

Rohan Das's FuunctionInput: 6

Rohan Das's Fuunction Output: 
[6, 12, 18, 26,....,60]

You have to write a function isCorrect(table,number) and return the index
whre Rohan's function is wrong and print it to the screen! If the
table is correct, your function return None.
'''

import random

def rohan_function(number):
    rndm = random.randint(3,9)
    mul_table = []

    for i in range(1,11):
        
        if i == rndm:
            mul_table.append((rndm*number)+2)
        else: mul_table.append(i*number)
    
    return mul_table


def isCorrect(table, number):
    correct_table = [x*number for x in range(1,11)]
    compare_table = [i for i,j in zip(table, correct_table) if i!=j]
    index_num = table.index(*compare_table)
    print(f'Error in table at index num {index_num}')
    print(f"{compare_table} is incorrect ")
    print(f"Correct table is ")
    print(correct_table)

    
if __name__ == '__main__':
    print("Multiplication Table")
    #num = input("Enter number: ")
    num = 7
    rohan_table = rohan_function(num)
    print("Rohan's Table Output" )
    print(rohan_table)
    print("Want to check output Correct or Not")
    ch = input("Enter Y/y to check and N/n to close: ")
    if ch=='y' or ch == 'Y':
        isCorrect(rohan_table, num)
    else:
        print("Good Bye")
    
    

            