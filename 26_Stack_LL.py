"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

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

    def insert_first(self, new_element):

        
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def print_stack(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next


    def delete_first(self):
       "Delete the first (head) element in the LinkedList as return it"

       if self.head:
            deleted_element = self.head
            temp = deleted_element.next

            self.head = temp 
            return deleted_element.value
       else:
           print("Else Statement")
           return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return (self.ll.delete_first())

    def display(self):
        "Display Stack List "
        self.ll.print_stack()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack()

# Test stack functionality
stack.push(e1)
stack.push(e2)
stack.push(e3)

stack.display()
print('\nThis element is deleted: ',stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# stack.push(e4)
# print(stack.pop())