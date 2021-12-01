# This implements quick sort using lomuto partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if len(elements)== 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

    return elements

def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index

if __name__ == '__main__':

    arr = [98,23,76,12,90,32,1,9,2,7,6,3]
    print('Unsorted Array ',arr)

    print("Sorted Array", quick_sort(arr,0, len(arr)-1))

    
    