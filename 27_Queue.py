"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)


    def peek(self):
        return self.storage[0]

    def dequeue(self):

        del_val = self.storage[0]

        self.storage.pop(0)
        return del_val
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print('Peek: ',q.peek())

# Test dequeue
# Should be 1
print('Dequeue ',q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print('Dequeue ',q.dequeue())
# Should be 3
print('Dequeue ',q.dequeue())
# Should be 4
print('Dequeue ',q.dequeue())
q.enqueue(5)
# Should be 5
print("Peek ",q.peek())