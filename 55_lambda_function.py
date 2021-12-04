# x=lambda x: x+15
# y = lambda y: y*15
# print(y(x(6)))
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
arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]

arr3 = list(filter(lambda x: x in arr1, arr2))
print(arr3)
