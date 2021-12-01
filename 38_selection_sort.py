def selection_sort(elems):
    start = 0

    if len(elems)==1:
        return elems
    elif len(elems) < 1:
        return elems
    while start < len(elems) -1:
        for j in range(start+1, len(elems)):
            if elems[j] < elems[start]:
                elems[j], elems[start] = elems[start], elems[j] 
        
        start = start + 1
    return elems

if __name__ == "__main__":
    test = [[],[32],[23,1,2,3,1,2,3],[98,23,76,12,90,32,1,9,2,7,6,3]]
    for test in test:
            
        print("Unsorted List: ", test)
        print("Sorted List: ", selection_sort(test))
        # print("Sorted List: ", test[3])