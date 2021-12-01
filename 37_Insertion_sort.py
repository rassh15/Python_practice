def insertion_sort(elems):
    for i in range(1,len(elems)):
        anchor = elems[i]
        j = i -1

        while j>=0 and anchor < elems[j]:
            elems[j+1] = elems[j]
            j = j - 1

        elems[j+1] = anchor
    return elems


if __name__ == "__main__":
    test = [[],[32],[23,1,2,3,1,2,3],[98,23,76,12,90,32,1,9,2,7,6,3]]

    print("Unsorted List: ", test[3])
    print("Sorted List: ", insertion_sort(test[3]))