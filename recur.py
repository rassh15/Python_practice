#recursion

# def func1(n):
#     print("Calling from func1", n)


# def func2(n):
#     if n > 0:
#         n = n - 1
#         print("first recursion: ", n)
#         func2(n)
#         n = n - 3
#         print("second recursion: ", n)
#         func2(n)
#         print('After: func2 ', n)

#         func1(n)


# func2(8)

from typing import Hashable


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def getitemhash(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def setitemhash(self, key, val):
        h =  self.get_hash(key)
        found = False

        for idx, elem in enumerate(self.arr[h]):
            if len(elem) == 2 and elem[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key,val))

    def displayArr(self):
        for i in self.arr:
            print(i)


t = HashTable()
# t['March 6'] = 120
# t['March 6'] = 78
# t['March 8'] = 67
# t['March 9'] = 4
# t['March 17'] = 459
t.setitemhash('March 6', 120)
t.setitemhash('March 6', 15)
t.setitemhash('March 8', 18)
t.setitemhash('March 9', 215)
t.setitemhash('March 17', 315)
t.setitemhash('March 17', 3)


t.displayArr()
print(t.getitemhash('March 6'))
