#Merge sort using python

def merge_sort(arr):
    if len(arr)> 1:
        print(len(arr))
        #Divide arrray into two halves
        mid = len(arr)//2

        #Temp arrays0
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        print("Before Calling function")
        print('l_arr', l_arr)
        print('r_arr', r_arr)

        merge_sort(l_arr)
        print("After L_arr Calling function")
        print('l_arr', l_arr)
        print('r_arr', r_arr)

        merge_sort(r_arr)
        print("After R_arr Calling function")
        print('l_arr', l_arr)
        print('r_arr', r_arr)
        
        i = j = k = 0

        while i<len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                print('arr[k] ',k ,' ',arr[k])
                i += 1
            else:
                arr[k] = r_arr[j]
                print('arr[k] ',k ,' ',arr[k])
                j += 1
            k += 1
        
        while i < len(l_arr):
            arr[k] = l_arr[i]
            print('arr[k] ',k ,' ',arr[k])
            k += 1
            i += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            print('arr[k] ',k ,' ',arr[k])
            k += 1
            j += 1

        print('arr',arr)
        
    

if __name__ == '__main__':

        
    test_array = [ 76,23,45,12,345,657,98,34,44,23,534]

    print("Array: ", test_array)
    merge_sort(test_array)

    print("Sorted Array: ", test_array)