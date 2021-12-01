'''
Harry has got an n number of apples. Harry has some students
among whome, he wants to distribute the apples. These
n number of apples are provided to harry by his 
friends and he can request for few more or few less apples.

You need to print whether a number in range mn to mx is 
a divisor of n or not.

Input: n, mn, and mx from the user
Output: Print whether numbers between mn and mx are
divison of n or not

Example: n = 20 , mn = 2 , mx = 5
2 is a divisor of 20
3 is not a divisor of 20
..
5 is a divisor of 20


'''

# Inputs

n, mn, mx = map(int, input('Enter values seperate by space: ').split())
output = False
for i in range(mn, mx+1):
    if n%i == 0:
        print(f"{i} is a divisor of {n}")
        output=True 
    else:
        print(f"{i} is not a divisor of {n}")

if output==False:
    print("Given range does not divide the the number equally\n Please try with another range")