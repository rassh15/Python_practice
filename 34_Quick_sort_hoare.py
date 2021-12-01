
# This quick sort using Hoare Partition scheme
#01 In which first element is select as pivot 
#02 Increase start pointer till element found greate then pivot
#03 decrese end pointer till element found less then pivot elemt
#04 swap start and end pointer value
#05 Repeat above steps
#06 End process when end pointer cross start pointer
#07 Swap the end pointer value to pivot
#08 Repeat above till list get sorted

def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp

def partition(elem, start, end):

    pivot_index = start
    pivot = elem[pivot_index]
    while start < end:
        while elem[start] <= pivot and start<len(elem)-1:
            start += 1
        while elem[end] > pivot and end>0:
            end -= 1

        if start < end:
            swap(elem,start, end)
    swap(elem ,pivot_index, end)

    return end

def quick_sort(elem,start, end):
    if start < end:
            
        pi = partition(elem, start, end)

        quick_sort(elem, start, pi-1) #left list
        quick_sort(elem, pi+1, end) #right list
    return elem




if __name__ == "__main__":
    arr = [98,23,76,12,90,32,1,9,2,7,6,3]
    print('Unsorted Array ',arr)

    print("Sorted Array", quick_sort(arr,0,len(arr)-1))