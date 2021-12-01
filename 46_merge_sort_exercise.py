
def merge_sort(elems, key='age', descending=False):
    if len(elems)<1: return "Empty"

    if len(elems)==1: return elems

    mid = len(elems)//2

    left = elems[:mid]    
    right = elems[mid:]
    

    merge_sort(left)
    merge_sort(right)

    i = j = k =  0

    if descending:

        while i < len(left) and j < len(right):
            if left[i][key] >= right[j][key]:
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
    else:
        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
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

    # test = [[],[32],[23,1,2,3,1,2,3],[98,23,76,12,90,32,1,9,2,7,6,3]]
    
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    merge_sort(elements)

    for i in elements:
        print(i)