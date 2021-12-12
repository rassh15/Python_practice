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
'''Olist = [2, 4, -6, -9, 11, -12, 14, -5, 17]

print('Neg ',sum(list(filter(lambda x: x<0,Olist))))
print('Pos ',sum(list(filter(lambda x: x>0,Olist))))
'''

# find the list with maximum and minimum length using lambda.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
'''arr1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
tmp1 = len(arr1[0])
for x in arr1:
    if len(x) > tmp1:
        tmp1 = len(x)
        arrmax = x

for x in arr1:
    if len(x) < tmp1:
        tmp1 = len(x)
        arrmin = x

print(arrmin, ' ', arrmax)

#using lambda
max_list = max(arr1, key = lambda i: len(i))
min_list = min(arr1, key = lambda i: len(i))
print(max_list,' ',min_list)
'''

#  sort each sublist of strings
#  [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
'''arr1 = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

result = [sorted(x, key = lambda x:x[0]) for x in arr1] 
print(result)

'''

#  sort a given list of lists by length and value
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
'''orlist =  [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17, 8]]
sortlistlen =[sorted(x, key= lambda x: x) for x in orlist]
# sortlistlen.sort()
print(sortlistlen)
#also using tuple as key
result = sorted(orlist, key=lambda l: (len(l), l))
print(result)'''

#  maximum value in a given heterogeneous list using lambda. Go to the editor
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximu= 5
'''arr1 = ['Python', 3, 2, 4, 5, 'version']
print(max(list(filter(lambda x: isinstance(x,int), arr1))))
'''
# sort a given matrix in ascending order according to the sum of its rows using lambda. Go to the editor
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
'''
arr1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
arr1 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(sorted(arr1, key= lambda x: sum(x)))

'''

#  extract specified size of strings from a give list of string values using lambda. Go to the editor
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']
'''arr1 =  ['Python', 'list', 'exercises', 'practice', 'solution']
print(list(filter(lambda x: len(x)==4, arr1)))'''

#  count float number in a given mixed list using lambda. Go to the editor
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of floats in the said mixed list:
# 3
'''arr1 =  [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(len(list(filter(lambda x: isinstance(x,float), arr1))))
'''

#  check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Go to the editor
# Input the string: W3resource
# ['Valid string.']
'''str1 = 'W3resource'
messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
m2 = [i(str1) for i in messg]

result = [x for x in m2 if x!=True]
print(result)
if not result:
        result.append('Valid string.')
print(result)

'''

# filter the height and width of students, which are stored in a dictionary using lambda. 
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height> 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
'''dict1 = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

print(dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), dict1.items())))
'''

# extract the nth element from a given list of tuples using lambda. Go to the editor
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
'''
arr1 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

print(list(map(lambda x: (x[0]),arr1)))

'''
#  sort a list of lists by a given index of the inner list using lambda
'''arr1 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n=1
print([sorted(arr1, key= lambda x: (x[n]))])'''

# remove all elements from a given list present in another list using lambda. Go to the editor
# Original lists:
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2= [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]
'''list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2= [2, 4, 6, 8]
list(filter(lambda x: list1.remove(x), list2))
print(list1)
result = list(filter(lambda x: x not in list2, list1))
'''
# find the nested lists elements, which are present in another list using lambda.
# Original_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# slist =  [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]

'''print([list(filter(lambda x: x in Original_lists, sublist))for sublist in slist])

'''

#  reverse strings in a given list of string values using lambda. Go to the editor
# Original lists:
'''stra = ['Red', 'Green', 'Blue', 'White', 'Black']

print(list(map(lambda x: x[::-1], stra)))
'''

# calculate the product of a given list of numbers using lambda. Go to the editor
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Product of the said list numbers:
# 3628800
'''list1 = [4, 3, 2, 2, -1, 18]
print(reduce(lambda x,y: x*y, list1))'''

# calculate the average value of the numbers in a given tuple of tuples using lambda. Go to the editor
# Original Tuple:
# ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)'''
'''stl =  ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))

print(tuple(map(lambda x: sum(x) / float(len(x)), zip(*stl))))'''

# convert string element to integer inside a given tuple using lambda. Go to the editor
# Original tuple values:
# (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))
'''
arr1 = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
print(tuple(map(lambda x: (int(x[0]), int(x[2])), arr1)))'''

# index position and value of the maximum and minimum values in a given list of numbers using lambda. Go to the editor
# Original list:
'''og = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
mx = max(og ,key = lambda x:x)
print((og.index(mx),mx))
mn = min(og ,key = lambda x:x)
print((og.index(mx),mn))
print(max(enumerate(og), key=lambda x:x[1]))
print(min(enumerate(og), key=lambda x:x[1]))'''

# sort a given list of strings(numbers) numerically using lambda. Go to the editor
# Original list:
'''arr1 = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
print(sorted(arr1, key=lambda x: int(x))'''

#  count the occurrences of the items in a given list using lambda. Go to the editor
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

'''arr1 =  [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
from collections import Counter
print(Counter(arr1))
print(dict(map(lambda el  : (el, list(arr1).count(el)), arr1)))
'''

#  remove specific words from a given list using lambda. Go to the editor
# Original list:
# ['orange', 'red', 'green', 'blue', 'white', 'black']
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']
'''
arr1 = ['orange', 'red', 'green', 'blue', 'white', 'black']
arr2 = ['orange', 'black', 'red']
print(list(filter(lambda word: word not in arr2,arr1 )))
'''
# remove None value from a given list using lambda function. Go to the editor
# Original list:
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]
'''arr1 =  [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

print(list(filter(lambda x: x is not None, arr1)))'''

#find max and min from given list
'''arr1 = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print(max(arr1,key=lambda item:item[1])[1])
print(min(arr1,key=lambda item:item[1])[1])'''


# sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
'''og = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print(sorted(og, key=lambda x: str(x)))
'''
