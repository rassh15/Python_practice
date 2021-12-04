#reverse list
list1 = [100, 200, 300, 400, 500]

print(list1[::-1])

#concatenate two list
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)

#concatenate two list using zip
print([i + j for i, j in zip(list1,list2)])

#square of list
numbers = [1, 2, 3, 4, 5, 6, 7]
print([x*x for x in numbers])

#contaneate 
ag1 = ["Hello ", "take "]
ag2 = ["Dear", "Sir"]
ag3 = []

for i in ag1:
    for j in range(len(ag2)):
        ag3.append(i+ag2[j])
print(ag3)

#using list comprehension
print([x + y for x in ag1 for y in ag2])

lt1 = [10, 20, 30, 40]
lt2 = [100, 200, 300, 400]

for a,b in zip(lt1,lt2[::-1]):
    print(a,b)

# Remove empty strings from the list of strings
st1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# [st1.remove(x) for x in st1 if x==""]
# print(st1)

#using filter function
print(list(filter(None, st1)))

# add item 7000 after 6000 in the following Python List
t1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

t1[2][2].append(7000)
print(t1)

la1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
for x in sub_list:
    la1[2][1][2].append(x)
print(la1)

ist1 = [5, 10, 15, 20, 25, 50, 20]
index = ist1.index(20)
ist1[index] = 200
print(ist1)

# remove all occurrences of item 20.

sq1 = [5, 20, 15, 20, 25, 50, 20]

for i in sq1:
    if i==20:
        sq1.remove(i)
print(sq1)
#list comphrehension

sq11 = [5, 20, 15, 20, 25, 50, 20]
print([i for i in sq11 if i!=20])

