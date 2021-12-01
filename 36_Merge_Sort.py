
def merge_sort(elems):
    if len(elems)<1: return "Empty"

    if len(elems)==1: return elems

    mid = len(elems)//2

    left = elems[:mid]    
    right = elems[mid:]
    

    merge_sort(left)
    merge_sort(right)

    i = j = k =  0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            elems[k] = left[i]
            i += 1
            k += 1
        else:
            elems[k] = right [j]
            j = j+1
            k += 1
    
    while i< len(left):
        elems[k] = left[i]
        i += 1
        k += 1

    
    while j< len(right):
        elems[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':

    test = [[],[32],[23,1,2,3,1,2,3],[98,23,76,12,90,32,1,9,2,7,6,3]]
    
    for test in test:
        print('Unsorted Array ',test)
        merge_sort(test)
        print('Sorted Array ',test)