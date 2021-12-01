def binary_search(array,val):
    print(array, ' ', val)

    start = 0
    end = len(arr)
    
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_search_recur(array, start, end, val):

    if end < start: return -1

    mid = (start + end) // 2
    
    if val == arr[mid]:

        return mid
    elif val > arr[mid]:
        start = mid + 1
    else: end = mid - 1

    return binary_search_recur(array, start, end, val)


def linear_search(array,val):
    for i in range(len(array)):
        if val==array[i]: return i
    return -1



if __name__ == '__main__':
    arr = [12,34,56,78,90,123,234,456,678,890,999]
    val = 678

    print('Using Binary Search',binary_search(arr,val))
    print('Using Linear Search',linear_search(arr,val))
    ind = binary_search_recur(arr,0, len(arr), val)
    print("using Binary Recursion", ind)
    