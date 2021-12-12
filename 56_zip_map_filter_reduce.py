# zip
'''def average_tuple(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result

nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
for i in zip(nums):
    print(i)

for i in zip(*nums):
    print(sum(i)/float(len(i)))
for i in nums:
    print(i)


'''

nums1 = [1,2,4,6,8,10,12,14,16,17]
original_lst = ['Red', 'Blue', 'Black', 'White', 'Pink']
# triple all numbers of a given list of integers Use Python map

print(list(map(lambda x: x*3, nums1)))

#  listify the list of given strings individually 
print(list(map(list, original_lst)))
# create a list containing the power of said number in bases raised to the corresponding number in the index using Python map

arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: x[0]**x[1],zip(arr1,arr2))))
print(list(map(pow, arr1, arr2)))

# convert all the characters in uppercase and lowercase and eliminate duplicate letters 

d1 = {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

print(dict(map(lambda x: (x,x.upper()), d1)))

print(list(map(lambda x: ((x[0]-x[1]), (x[0]+x[1])), zip(arr1,arr2))))

arr5 = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'), ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]
n=1
print(list(map(lambda x: x[n],arr5)))

# convert a given list of tuples to a list of strings using map function
# Original list of tuples:
# [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']
'''arrt = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

print(list(map(lambda x: x[0]+' '+x[1], arrt)))'''

# split a given dictionary of lists into list of dictionaries using map function.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
'''
ordic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
dt = dict()
lt = list()
for key, value in ordic.items():
    for val in value:
        lt.append([key,val])
print(*zip(lt))
print(list(map(dict,zip(*[lt]))))

print(list(map(dict, zip(*[[(key, val) for val in value] for key, value in ordic.items()]))))
'''
#  interleave two given list into another list randomly using map() 
# Original lists:
'''arri = [1, 2, 7, 8, 3, 7]
arrj = [4, 3, 8, 9, 4, 3, 8, 9]

import random
print(list(map(lambda x: random.choice(x),arrj)))
'''

# Original lists:
'''a1= [1, 2, 3, 4, 5, 6, 7, 8]
a2= [2, 2, 3, 1, 2, 6, 7, 9]

from operator import eq
result = map(eq, a1, a2)
for m in result:
    print(m)
'''
i=5
print(++i)
# ab = []
# for i in range(10):
#     ab.append(i* ++i)
# for ab[i] in ab:
#     print(ab[i])

from functools import reduce


# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]


# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]


# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]


# Fix all three respectively.
map_result = list(map(lambda x: round(x*x,3), my_floats))
filter_result = list(filter(lambda name: len(name)==7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)


print(map_result)
print(filter_result)
print(reduce_result)