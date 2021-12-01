'''
You visit a restaurant called CodeWithHarry and food items
in this restaurant are sorted based on their amount of 
calories. YOu have to reverse this list of food items
and their calories.

You have to use following three methods to reverse it:
- Inbuilt method
- Slicing trick
- Swapping first element with last one
and second element with second last element and so on...


'''

#numb_list = list(map(int, input('Enter list element seperated by space: ').split()))
numb_list = [2, 9, 8, 7, 3, 6, 5, 15]
numb_list_copy = numb_list.copy()
numb_list_copy2 = numb_list.copy()

print('List before reverse:\n',numb_list)
#Reverse using slicing
slice_rev = numb_list[::-1]
print("List reverse with slicing method:\n",slice_rev)

#Reverse using inbuilt method
numb_list_copy.reverse()
print("Reverse using inbuilt method:\n",numb_list_copy)

#using inbuilt reverse function
# for i in reversed(numb_list):
#     print(i, end="")
# print()
len_list = len(numb_list)

using_slic_reverse= []
for i in range(-1, -(len_list+1),-1):
    using_slic_reverse.append(numb_list[i])

print("Using slicing reverse\n",using_slic_reverse)

mid = len_list//2
for i in range(mid):
    tmp1 = numb_list_copy2[i]
    tmp2 = numb_list_copy2[-(i+1)]
    numb_list_copy2[i] = tmp2
    numb_list_copy2[-(i+1)] = tmp1
print('Using replace list\n',numb_list_copy2)

if slice_rev == numb_list_copy and numb_list_copy == numb_list_copy2:
    print("All methods gives same result")
else: print("Error")