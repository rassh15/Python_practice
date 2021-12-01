def bubble_sort(arr):
    print(arr)
    cnt = 0
    

    for i in range(len(arr)-1):
        flag = 1
        for j in range(1 ,len(arr)):
            if arr[j-1] > arr[j]:
                flag = 0
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
        if flag == 1:
            return arr
        cnt = cnt + 1

        print(cnt,arr)

if __name__ == "__main__":
    arr = [98,23,76,12,90,32,1,9,2,7,6,3]

    print("Sorted Array", bubble_sort(arr))