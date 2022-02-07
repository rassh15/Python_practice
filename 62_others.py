'''
from collections import OrderedDict

numofitems = 9
iterlist = [('BANANA FRIES', 12),
("POTATO CHIPS", 3),
("APPLE JUICE", 10),
("CANDY", 5),
("APPLE JUICE ",10),
('CANDY', 5),
('CANDY', 5),
('CANDY', 5),
("POTATO CHIPS", 30),]
orderDict = OrderedDict()

for i,j in iterlist:
    if i in orderDict.keys():
        orderDict[i] = orderDict[i] + j
    else:
        orderDict[i] = j

print(orderDict)
# for items, value in orderDict.items():
#     print(f"{items} {value}")
'''
'''
import calendar
from datetime import datetime
# print(calendar.TextCalendar(firstweekday=0).formatyear(2015))

# for i in calendar.__dir__():
#     print(i)

dayindex = calendar.weekday(2021,12,13)
print(calendar.day_name[dayindex])
# dayname = list(calendar.day_name)
# for i in range(len(dayname)):
#     if i==dayindex:
#         print(dayname[i].upper())
                                                                                                      
'''
'''
import  re
from datetime import datetime


def time_delta(t1,t2):

    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))



t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'


print(time_delta(t1, t2))


a2 = '.*\+'
a1 = '.*+'
print(True) if re.compile(a1) else print(False)

'''

import fractions
import itertools
'''
#(1,2)(1,3)(1,4)(2,3)(2,4)(3,4)
strn = 'aacd'
strtup = 2
tuplist = list()
# for i in range(len(strn)):
for i in range(0,len(strn)):
    for j in range(i+1,len(strn)):
        tuplist.append((i,j))
print(tuplist)
cnta= 0
cntb = 0
a = itertools.combinations(strn,strtup)
for i in a:
    cnta += 1
    if 'a' in i:
        cntb += 1
print(cntb/cnta)
'''

'''
s = [7, 825,5]
lit = [[5182292, 7637290, 890394, 3370924, 7713560, 6636415, 1973586],
[9389142, 9685974, 4823607, 3909292, 4590796, 7794199, 3272076],
[8074994, 4764529, 9100216, 9236920, 4932416, 4918538, 1977304],
[5593202, 4697941, 3062476, 9967177, 3419823, 2702180, 7134227],
[631384, 4195172, 8254403, 5813676, 1832462, 9144797, 1700951],
[9546021, 5781211, 3674536, 1451514, 7983537, 8498142, 5360805],
[2574332, 8808693, 1149232, 649325, 6089573, 2765799, 2402597]]

# 824

# print(list(itertools.product(s)))
nums = []

for j in lit:
    nums.append(list(map(lambda x: (x**2)%825, j)))
    tl = list(map(lambda x: sum(x)%825, itertools.product(*nums)))

print(sum([1,2,3,5])%2)
# print(list(itertools.product(*[[1,2,3],[4,5,6]],[7,8,9])))
'''
from operator import itemgetter
lt = [["Mike Thomson",'20', 'M'],[
"Robert Bustle", '32'," M"],[
"Andria Bustle" ,'30', "F"]]
lt.sort(key=itemgetter(1))
# print(lt)
# a = itemgetter(1)
# print(a(lt))

x = [
 ['4', '21', '1', '14', '2008-10-24 15:42:58'], 
 ['3', '22', '4', '2somename', '2008-10-24 15:22:03'], 
 ['5', '21', '3', '19', '2008-10-24 15:45:45'], 
 ['6', '21', '1', '1somename', '2008-10-24 15:45:49'], 
 ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
]

from operator import itemgetter
'''
x.sort(key=itemgetter(1))

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: x[2]))          
    return inner


'''

import operator
    
'''




    
                                                    
def person_lister(f):
    def inner(people):

        lt = []
        for i in people:
            lt.append([i[0],i[1],int(i[2]),i[3]])
        # print(people)
        # print(lt)
       
        # lt.sort(key=operator.itemgetter(2))
        # return map(f,lt)
        people.sort(key=operator.itemgetter(2))
        return map(f,people)
        # return map(f, sorted(people, key=lambda x: x[2]))
        # return map(f, sorted([[e[0], e[1], int(e[2]), e[3]] for e in people], key=operator.itemgetter(2)))  
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [["Jake","Jake","42","M"],["Jake","Kevin","57","M"],["Jake","Michael","91","M"],["Kevin","Jake","2","M"],["Kevin","Kevin","44","M"],["Kevin","Michael","100","M"],["Michael","Jake","4","M"],["Michael","Kevin","36","M"],["Michael","Michael","15","M"],["Micheal","Micheal","6","M"]]    
    print(*name_format(people), sep='\n')
'''
'''
a1 = 121426 # Here, 1 is an alternating repetitive digit.
a2 = 523563 # Here, NO digit is an alternating repetitive digit.
a3 = 552523 # Here, both 2 and 5 are alternating repetitive digits.
import re
pattern = re.compile(r'(1\d1|2\d2|3\d3|4\d4|5\d5|6\d6|7\d7|8\d8|9\d9|0\d0)')
print(pattern.search(a1))


s=input()
print (bool(re.match(r'^[1-9][\d]{5}$',s) and len(re.findall(r'(\d)(?=\d\1)',s))<2 ))
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"
'''
'''
import re
# lt = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
lt = ["T%Mic&","h%axr%","iit#p!","ssrst&"]
strn = ''
for i in range(3):
    for j in range(len(lt)):
        strn += lt[j][i]

print(strn)
# output: This is Matrix#  %!
# ab = "This$#is% Matrix#  %!"
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ",strn))

'''
'''
for i in range(1, 6):
    for j in range(1,i+1):
        print(j, end=' ')
    for k in range(i-1,0,-1):
        print(k, end=' ')
    print()

import math

lt = [12,213,43,21,44,56,43,12,213]

s= set()

for i in lt:
    s.add(i)

print(len(s))
'''
s = set("Hacker")
print(s.union(enumerate(['R', 'a', 'n', 'k'])))
    #  .update()                      update
# .intersection_update()       intersection_update
# .difference_update()            difference_update
# .symmetric_difference_update()    symmetric_difference_update

'''
a = {1,2,4,6,7}
b = {1, 2,6,7,8}

print(a.difference(b).pop())

''''''

lt = [4, 3, 2, 1, 3, 4]


for i in range(len(lt)-1,0,-1):
    if lt[i] < lt[i-1] and lt[i] < lt[0]:
        print(0)
    elif lt[i] < lt[i-1] and lt[i] > lt[0]:
        '''

import numpy 
'''
a = np.array([[1,2],[3,4]])
prd = a.sum(axis=0)
print(np.prod(prd))


'''

sft ="B1CD102354"


import re

patt = '[A-z]{2,}\d{3,}'
print(re.search(patt,sft))
'''
B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid
'''
'''
for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
    '''
print()

u = '4123356789123456'

'''
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")



try:
    assert re.search(r'^[456]', u)
    assert re.search(r'[0-9]', u)
    assert not re.search(r'[\s_]', u)
    assert not re.search(r'^(\d)\1+$', u)
    assert len(u) == 16
except:
    print('Invalid')
else:
    print('Valid')
'''

s = "> and then she told him she wouldn't settle for less than a Hawaiian pizza, and"

print(re.search(r'(?<=[a-z])\d', 'geeksforgeeks15'))



s = 'this is python'
print(s[-1])

print(type((1)))
print(type((1,)))
i = 0
while i < 20:
    if i < 6:
        i = i + 1
        continue

    print(i)

    i = i + 1


# Python3 program for demonstrating
# coroutine execution
 
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)
 
# calling coroutine, nothing will happen
corou = print_name("Dear")
 
# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()
 
# sending inputs
corou.send("Dear James")
corou.send("Dear Mes")
# corou.send("Dear patul")
corou.close()

set1 = {10,20,30}
set2 = {10,20,30,'45',65,8}
print(set1.union(set2))


import numpy as np
def find_nearest_value(arr, value):
   arr = np.asarray(arr)
   print(arr)
   print(np.abs(arr))
   idx = (np.abs(arr - value)).argmin()
   return arr[idx]
#Driver code
arr = np.array([ -0.21169,  0.61391, 0.6341, 0.0131, 0.16541,  0.5645,  0.5742])
value = 0.52
print(find_nearest_value(arr, value))

def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1
print(add_nums(2, 10))

def print_pairs(arr, N):
       # hash set
   hash_set = set()
    
   for i in range(0, len(arr)):
       val = N-arr[i]
       if (val in hash_set):    #check if N-x is there in set, print the pair
           print("Pairs " + str(arr[i]) + ", " + str(val))
       hash_set.add(arr[i])

# driver code
arr = [1, 2, 40, 3, 9, 4]
N = 3
print_pairs(arr, N)



class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
first_name = "XYZ"
person = Person(first_name, "ABC")
first_name = "LMN"
person.last_name = "PQR"
print(person.first_name, person.last_name)


import copy
lt1 = [1, 2, [3,5], 4]
lt2 = copy.copy(lt1)

lt3 = copy.deepcopy(lt1)

lt2[2][0] = 12
lt2[3] = 19
lt3[2][0]  = 14

print(lt1)
print(lt2)
print(lt3)

class X:
    a = 1

X = type('X', (), dict(a=1))
print(X)

print('01 Deco')

def print_number(number):
    print(number)


assign_print_number = print_number


def test_decorator():
    assign_print_number(8)
    print_number(3)

test_decorator()

print('02 Deco')
class decorator_with_arguments(object):
    
    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("Donald", "Le", "1990")
def test_decorator_with_arguments():
    print("Testing decorator with arguments")

test_decorator_with_arguments()

print('03 Deco')
import datetime


def dot_and_at(func):
    def inner(*args, **kwargs):
        print("." * 30)
        func(*args, **kwargs)
        print("@" * 30)
    return inner


def time_shown(func):
    def inner(*args, **kwargs):
        print(f'Start time is {datetime.datetime.now()}')
        func(*args, **kwargs)
        print(f'End time is {datetime.datetime.now()}')
    return inner


@dot_and_at
@time_shown
def printer(msg):
    print(msg)


printer("Hello")


def test_decorator():
    printer("Test Decorator")
test_decorator()


lt = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

print(sorted(lt,key=lambda x:x[1]))
nlist = [10, 2, 5, 9, -1]
result = all(elem > 0 for elem in nlist)

print(result)

print(sorted('Sorting1234'))

a1 = 'aaadaa'
a2 = 'aa'
patt = re.compile(a2)
match = patt.findall(a1,)
print(match)

import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9 e r  s"))


ast = 'if a + b > 0 && a - b < 0:'

pa = re.compile(r'(?<= )(&&|\|\|)(?= )')
print(pa.search(ast))


import email.utils

a = email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print(a[1])

patt = re.search(r'^\w[A-za-z0-9-._]\@[A-Za-z]\.[A-Za-z]{1,3}', a[1])
print(patt)

s1= 'rabcdeefgyYhFjkIoomnpOeorteeeeet'


s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, s1, re.I)
print('\n'.join(a or ['-1']))

n = 5
a = 0
b = 1
sum = 0
count = 1
lt = []
print("Fibonacci Series: ", end = " ")
while(count <= n):
    lt.append(sum)
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b
print(lt)

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    print(words)
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                print('ly ',letter)
                num_vowels += 1
        print('num_vowels',num_vowels)
        print('Score ',score)        
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

words = 'programming is awesome'.split()
print(score_words(words))


patt = r'^[+-.]{0,}[.]{1}'
print(re.search(patt,'4.00'))