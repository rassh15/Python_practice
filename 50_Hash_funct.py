from typing import Hashable


class HashTable():

    def __init__(self):
        self.MAX = 100
        self.arr = [None for x in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, value): #set method python library
        hash = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))


    def __getitem__(self, key): #get method python library
        hash = self.get_hash(key)

        print(self.arr[hash])


t = HashTable()
t.__setattr__('mars44',152)
t.__setattr__('mars64',1223)
t.__setattr__('mars15',122234)
t.__setattr__('mars14',1122)
t.__setattr__('mars12',132)
t.__getitem__('mars64')

# t["Mass1"] = 182
# t['Mass2'] = 172
# t['Mass3'] = 162
# t['Mass4'] = 152
# t['Mass5'] = 142
# t['Mass6'] = 132
# t['Mass7'] = 122

