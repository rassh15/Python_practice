from typing import Counter


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        
        if self.head:
            while current.next:
                current = current.next
                
            current.next = new_element
        else:
            self.head = new_element




    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        counter = 1
        current = self.head
        
        if position > 1 :
            while current and counter <position:
                if counter == position -1:
                    new_element.next = current.next
                    current.next = new_element
                counter += 1
                current = current.next

        elif position ==1:
            new_element.next = current.next
            self.head = new_element

        
    def print_LL(self):
        current = self.head

        while current:
            print(current.value, end=' ')
            current = current.next
        
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None

        while current.value != value and current:

            previous = current
            current = current.next
        
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


e1= Element(5)
e2= Element(9)
e3= Element(7)
e4= Element(2)
e5= Element(78)

ll = LinkedList()
ll.append(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

print(ll.get_position(2).value)
print("Before Insertion: ")
print(ll.print_LL())

ll.insert(e5, 2)

print("After Insertion ")
print(ll.print_LL())

print(ll.get_position(2).value)

print("Before Deleting: ")

print(ll.print_LL())

ll.delete(78)

print("After Deleting: ")
print(ll.print_LL())
