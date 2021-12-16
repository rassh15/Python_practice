
# NumPy ufuncs
# ufuncs stands for "Universal Functions" and 
# they are NumPy functions that operates on the ndarray object.

# used to implement vectorization in NumPy 
# which is way faster than iterating over elements.
# has attribute like where , dtype and out

import numpy as np

# Without using ufunc
'''
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)
'''

# with ufunc
'''
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

x = np.add(x,y)
print(x)

# to create your own ufunc. first create normal function and the add it to
# frompyfunc() method it need three arg. frompyfunc(function, no. of input, no. of output)

def myfunc(x, y):
    return x+y

addfunc = np.frompyfunc(myfunc, 2, 1)
print(addfunc(1,5))
print(type(addfunc)) #to check function is ufunc or not
'''
# ufunc has Simple Arithmetic operation method
'''
np.add(arr1,arr2)
np.subtract(arr1,arr2)
np.multiply(arr1,arr2)
np.divide(arr1,arr2)
np.absolute(arr1,arr2)
'''
#and much more

# Rounding Decimals
# five ways of rounding off decimals in NumPy:

# truncation - np.trunc()
# fix - fix()
# rounding - around()
# floor - floor()
# ceil - ciel()

# Numpy logs
#  functions to perform log at the base 2, e and 1

# Cummulative Sum
# Cummulative sum means partially adding the elements in array.

# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)