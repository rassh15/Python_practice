#Bubble sort using python


def bubble_sort(input_array):
    print("Input Array: ", input_array)
    for j in range(len(input_array) - 1):
        for i in range(1, len(input_array)):

            if input_array[i-1] > input_array[i]:
                tmp = input_array[i]
                input_array[i] = input_array[i-1]
                input_array[i-1] = tmp
    return input_array
            


test_array = [ 76,23,45,12,345,657,98,34,44,23,534]

print("Sorted Array: ", bubble_sort(test_array))