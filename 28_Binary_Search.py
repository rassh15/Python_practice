"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def linear_search(input_array, value):
    """Your code goes here."""
    for i in range(0, len(input_array)):

        if input_array[i] == value:
            return i
    return -1


def binary_search(input_array, value):

    low = 0
    high = len(input_array)
    while low <= high:
        mid = (low + high)//2
        if input_array[mid] == value:
            return mid
        elif value > input_array[mid]:
            low = mid + 1
        else: high = mid - 1
    return -1

test_list = [1,3,9,11,15,19,29,34,56,76,89,98,99]
test_val1 = 76
test_val2 = 65
print(linear_search(test_list, test_val1))
print(linear_search(test_list, test_val2))
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))