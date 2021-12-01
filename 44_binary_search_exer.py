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

def find_all_occurrence(input_array, value):
    index = binary_search(input_array, value)

    indices =  [index]
    i = index - 1 # Find value on left side

    while i >= 0:
        if input_array[i] == value:
            indices.append(i)
        else:
            break
        i = i - 1

    j = index + 1
    while i < len(input_array):
        if input_array[i] == value:
            indices.append(i)
        else:
            break

        i += 1

    return sorted(indices)


test_list = [1,3,9,11,15,19,29,34,56,76,76,76,89,98,99]
test_val1 = 76
# print(binary_search(test_list, test_val1))
print(find_all_occurrence(test_list, test_val1))