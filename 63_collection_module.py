from collections import Counter
import imp

print(Counter(['A','A','A','B','B','B','C','C','C']))
print(Counter({'A':34,'B':22,'C':9}))
print(Counter(A=3,B=2,C=9))


from collections import OrderedDict


d2 = dict()

d2['A'] = 32
d2['B'] = 9
d2['C'] = 2
d2['D'] = 38
print('\nDictionary')
for key, value in d2.items():
    print(key, value)

d1 = OrderedDict()

d1['A'] = 32
d1['B'] = 9
d1['C'] = 2
d1['D'] = 38
print('\nOrdered Dictionary')
for key, value in d1.items():
    print(key, value)


from collections import ChainMap
print('\nChain Map')
c = ChainMap(d1,d2)
print(c)


from collections import deque
print('\nDeque')
q = deque([1,2,4,2,12,543,53])
print(q)


print("\nUserDict")
from collections import UserDict
from collections import UserList
from collections import UserString
    
'''
# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):
       
    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
           
    # Function to stop pop from 
    # dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
           
    # Function to stop popitem 
    # from Dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")
       
# Driver's code
d = MyDict({'a':1,
    'b': 2,
    'c': 3})
   
# d.pop(1)
'''


from collections import namedtuple

# student = namedtuple('student',['name','age','dob'])

# student = namedtuple('student','name age dob')
student = namedtuple('student','name ,age ,dob')

s = student('ras','12','121212')
s11 = student('as','123','433443')
print(s)
print(s11)


from collections import defaultdict

def default_val():
    return "Not Present"

d3 = defaultdict(default_val)

d3['A'] = 3
d3['E'] = 2

print(d3['A'])
print(d3['D'])


# Defining the dict
d4 = defaultdict(lambda: "Not Present")
d4["a"] = 1
d4["b"] = 2
print(d4)
print(d4['a'])
print(d4['d'])
# Provides the default value
# for the key
print(d4.__missing__("b"))
print(d4.__missing__('d'))
print(d4['a'])
print(d4['d'])


d5 = defaultdict(int)
d5['A'] = d5['A'] * 5
print(d5)


