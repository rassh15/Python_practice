'''
Patter priting
for given N integer and boolean = "True" or "False"

example:
given n = 4 and boolean = True

*
**
***
****

and for false

****
***
**
*

'''


numb_rows = int(input('Enter number of rows you want: '))
n = numb_rows
Boolean_operation = input('Enter operation True or False: ')

if Boolean_operation == "T":
        
    for i in range (1, n+1):
        print()
        for j in range(0,i):
            print('*',end=' ')
elif Boolean_operation == "F":
        
    for i in range(n+1, 0, -1):
        print()
        for j in range(i, 1, -1):
            print('*', end=' ')
else:
    print("Wrong Inputs")