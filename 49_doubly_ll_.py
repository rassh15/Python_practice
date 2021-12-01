class Node():
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class doubly_ll():
    def __init__(self):
        self.head = None

    def insert_at_beg(self, value):
        
        if self.head:
            node = Node(value, self.head)
            self.head.prev = node
            self.head = node

        else:
            self.head = Node(value)

    def insert_at_end(self, value):
        
        if self.head:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(value, None, itr)
        else:
            self.head = Node(value)

    def insert_at_index(self, index, value):
        if index > self.get_length():
            return "Invalid Index"
        elif index == 1:
            self.insert_at_beg(value)
        else:
            itr = self.head
            count = 1
            while itr:
                if count == index:
                    prev = itr.prev
                    node = Node(value, itr, prev)
                    itr.prev = node
                    prev.next = node
                count += 1
                itr = itr.next

    
    


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward_dll(self):

        itr = self.head

        while itr:
            print(f"{itr.data}-->",end='')
            itr = itr.next

    def print_backward_dll(self):
        itr = self.head

        while itr.next:
            itr = itr.next

        tail = itr

        while tail:
            print(f"{tail.data}-->",end=' ')
            tail = tail.prev





ll = doubly_ll()

ll.insert_at_beg(78)
ll.insert_at_beg(65)
ll.insert_at_beg(34)
ll.insert_at_end(32)
ll.insert_at_beg(12)
ll.insert_at_beg(44)
ll.insert_at_end(98)
ll.insert_at_index(2,39)
ll.insert_at_index(3,87)
print(ll.insert_at_index(12,312))
ll.print_forward_dll()
print()
ll.print_backward_dll()
print('\nLength of DLL: ',ll.get_length())
# ll.insert_at_end(98)
# ll.insert_at_end(100)
