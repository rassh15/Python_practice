#numpy library

import numpy as np
arr0 = np.array(0) # 0-D array
arr1 = np.array([1,2,3,4,5]) #1-D array
arr2 = np.array((1,2,3,4,5)) #1-D array
arr3 = np.array([[3,4,5,6,7],[6,3,1,5,3]]) #2-D array
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3-D array

# print(f"O-D {arr0}\n1-D {arr1}\n2-D {arr3}\n3-D {arr4}")

# print(f"Dimension {arr0.ndim} {arr1.ndim} {arr3.ndim} {arr4.ndim}")

#array can have any number of dimnension

arr5 = np.array([1,2,3,4,],ndmin=5)
# print(arr5.ndim)

# Indexing (accessing array) | you can also use negative indexing
'''
print(arr2[1])
print(arr3[1,2])
print(arr4[1,1,2])'''

# Slicing   [start:end] and  [start:end:step]
'''
print(arr1[3:5])
print(arr2[1:5:2])
print(arr2[::2]) #by default start and end value is 0 and len(array) 
'''
#Slicing 2D array
'''
print(arr3[1,1:3])
print(arr3[:,4])
'''

#Data types in numpy i=integer u = unsigned integer S=string
'''print(arr1.dtype)#to know the type of array

arr6 = np.array([1,2,3,4,5,6],dtype='S')
print(arr6)
'''
#You can also define size with following i, u, f, S and U
'''
arr7 = np.array([1,2,4,5,6], dtype='i4')
print(arr7)'''

#Converting Data Type on Existing Array
#CAN BE DONE BY make a copy of the array with the astype() method
'''
arr8 = np.array([1.1, 2.1, 3.1])
newarr = arr8.astype('i')# or astype(int)
print(newarr)
print(newarr.dtype)

arr9 = np.array([1, 0, 3])

newarr1 = arr9.astype(bool)

print(newarr1)
print(newarr1.dtype)
'''

# copy and view
#copy data  not affect original data
'''
x = arr2.copy()
arr2[0] = 42
print(arr2)
print(x)

#view data will affect original data vice versa
y = arr2.view()
arr2[1] = 12
print(arr2)
print(y)
#checks who owns the data copy or view. return None if owns else return array
print(x.base, y.base)

'''

# shape (return no. of elements in particular dimension)

"""
print(arr3.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
"""

#reshape
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr1 = arr.reshape(4, 3)# 1D to 2D

newarr2 = arr.reshape(2, 3, 2)# 1D to 3D

print(newarr1)
print(newarr2)

#we can pass -1 if dimension is unknown
print(arr.reshape(2,2,-1))

#Flatterning array (means convert multidimensional array into 1 D )
print(arr4.reshape(-1))
'''

#iterating over array

#simple using for loop or by using nditer()
'''
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

'''
# arr = np.array([1,2,3,4])
#op_dtypes used to change datatype while iterating
# here flag=buffered is used because numpy does change datatype inplace it require 
# some space to perform operation, extra space is called buffer for this flag is used
'''
for x in np.nditer(arr, flags = ['buffered'], op_dtypes=['S']):
    print(x)

#iter with different step size
for x in np.nditer(arr3[:, ::2]):
      print(x)

#iterate over with enemuerate
for idx, x in np.ndenumerate(arr3):
  print(idx, x)
'''

#  Joining 
'''
arrjoin = np.concatenate((arr1,arr2))
print(arrjoin)

arr11 = np.array([[1, 2], [3, 4]])

arr22 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr11, arr22), axis=1)
print(arr)


arr12 = np.array([1, 2, 3])

arr23 = np.array([4, 5, 6])

arr12s = np.stack((arr12, arr23)) # stack one another
print(arr12s)

arr12hs = np.hstack((arr12, arr23)) #stack along rows
print(arr12hs)

arr12hv = np.vstack((arr12, arr23)) #stack along column
print(arr12hv)

arr12hd = np.dstack((arr12, arr23)) #stack along height
print(arr12hd)


'''

# Splitting

#split using array_split()
#it return list array of array can access array[0]
'''print(np.array_split(arr2,3))

print(np.array_split(arr3,2)) # also use axis = 1 if needed
'''
# htack() ,vstack() and dstack() are available as hsplit(), vsplit() and dsplit()

# Searching
# Search an array using where() method

arrq = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arrq == 4)
# x = np.where(arr%2 == 0)
print(x)#will return index value

# searchsorted()  it allows to specify where specific value should be inserted

arr = np.array([6, 7, 8, 9])

x1 = np.searchsorted(arr, 7)
x2 = np.searchsorted(arr, 7, side='right') #also provide search side
x3 = np.searchsorted(arr, [9, 7, 6]) # can search multiples values

print(x3)

print(x1)
print(x2)


