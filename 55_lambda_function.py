# x=lambda x: x+15
# y = lambda y: y*15
# print(y(x(6)))
from functools import reduce


lt1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
lt1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

lt1.sort(key=lambda x:x[1])
print(lt1)


lt1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

lt1.sort(key= lambda x:x['color'])
print(lt1)

even = filter(lambda y:y%2==0, lt1)
odd= filter(lambda x:x%2!=0, lt1)
print(list(even))
print(list(odd))
'''
# print(list(map(lambda x:x**2, lt1)))
# print(list(map(lambda x:x**3, lt1)))

# program to find if a given string starts 
# with a given character using Lambda
'''stringa = 'this is the given string'
y = lambda x:x[0]=='q'
print(y(stringa))
start = lambda x: True if x.startswith('P') else False
print(start('Tha'))
'''
#  program to extract year, month, date and time using Lambda
'''import datetime

now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()

print(year(now))
print(month(now))
print(day(now))
print(time(now))

'''
#  check whether a given string is number or not using Lambda
'''
st1 = lambda x: x.replace('.','',1).isdigit()
st2 = lambda x: st1(x[1:]) if x[0] == '-' else st1(x)

print(st2('2.342'))
print(st2('4342'))
print(st2('sa2342'))
print(st2('-12547'))'''

# Fibonacci series upto n using Lambda
# series upto 9:[0, 1, 1, 2, 3, 5, 8, 13, 21]
# print(functools.reduce(lambda a, b: a if a > b else b, lis))
# reduce(fun,seq)
'''n1 = -1
n2 = 1
th = 15
for i in range(th):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
from functools import  reduce
fibx = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print(fibx(8))
'''

# find intersection of two given arrays using Lambda. Go to the editor
#  filter(function, sequence)
# Original arrays:
'''arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]

arr3 = list(filter(lambda x: x in arr1, arr2))
print(arr3)'''

# Original arrays:
array_nums = [-1,54,12,43, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# # [2, 5, 7, 8, 9, -10, -3, -1]
# st =  [-1, 2, -3, 5, 7, 8, 9, -10]

'''# reduce(lambda x: x.insert())
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)'''


# count the even, odd numbers in a given array of integers using Lambda
'''even = filter(lambda y:y%2==0, lt1)
odd= filter(lambda x:x%2!=0, lt1)
print(len(list(even)))
print(len(list(odd)))'''
# find the values of length six in a given list using Lambda
'''weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list6 = filter(lambda x: len(x)==6, weekdays)
print(list(list6))
'''
# add two given lists using map and lambda. Go to the editor
# Original list:
'''arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

print(list(map(lambda x,y: x+y , arr1, arr2)))
'''
#  find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda
'''arr1 = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

result=sorted(arr1, key=lambda x: x[1])
print(result[len(result)-2][0])'''

# find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
# Orginal list:
'''arr1= [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(list(filter(lambda x: x%13==0 or x%19==0, arr1)))
'''

#  find palindromes in a given list of strings using Lambda. Go to the editor
# Orginal list of strings:
'''strlist = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print(list(filter(lambda x: x[::-1]==x, strlist)))'''

# find all anagrams of a string in a given list of strings using lambda.
# Orginal list of strings:
'''strlist = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
strword = 'abcd'
print(list(filter(lambda x: sorted(x) == sorted(strword),strlist)))
in place of sorted counter can also be used
from collections import  Counter
print(Counter('abcd')==Counter('dcba'))'''

#  find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem. Go to the editor
# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
'''strl = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
print(sorted(list(map(int,list(filter(lambda x: x.isdigit() ,strl.split(' ')))))))'''

# multiply each number of given list with a given number using lambda function
'''Originallist = [2, 4, 6, 9, 11]
Givennumber = 2
print(list(map(lambda x: x*Givennumber, Originallist)))'''
#  sum the length of the names of a given list of names after removing the names that starts with an lowercase letter
'''
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
result = list(filter(lambda x: x[0].isupper() and x[1:].islower(), sample_names))
print(len(''.join(result)))

'''

#  calculate the sum of the positive and negative numbers of a given list of numbers using lambda function. 
Olist = [2, 4, -6, -9, 11, -12, 14, -5, 17]

print('Neg ',sum(list(filter(lambda x: x<0,Olist))))
print('Pos ',sum(list(filter(lambda x: x>0,Olist))))















