#Implementation of quick sort

# def partition(start, end , arr):
#     pivot_index = start
#     pivot = arr[pivot_index]

#     while start < end:
        
#         while start < len(arr) and arr[start] <= pivot:
#             start += 1
        
#         while arr[end] > pivot:
#             end -= 1

#         if start < end:
#             arr[start], arr[end] = arr[end], arr[start]

#     arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

#     return end

# def quick_sort(start, end, arr):

#     p = partition(start, end, arr)

#     quick_sort(start, p-1, arr)
#     quick_sort(p+1, end, arr)

# Python3 implementation of QuickSort  
  
# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end
      
# The main function that implements QuickSort 
def quick_sort(start, end, array):
      
    if (start < end):
          
        # p is partitioning index, array[p] 
        # is at right place
        p = partition(start, end, array)
          
        # Sort elements before partition 
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)




if __name__ == '__main__':
    
        
    test_array = [ 76,23,45,12,345,657,98,34,44,23,534]

    print("Array: ", test_array)
    quick_sort(0,len(test_array)-1,test_array)

    print("Sorted Array: ", test_array)