
class Node():
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


class linked_list():

    def __init__(self):
        self.head = None


    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def insert_at_given_index(self, index, data):
        
        if index > self.get_length():
            return 'Invalid Index'
        elif index == 1:
            self.insert_at_beg(data)

        else:
                
            count = 1
            itr = self.head
            while itr and count < index:
                if count == index-1:
                    tmp = itr.next
                    itr.next = Node(data,tmp)
                count += 1
                itr = itr.next


    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def delete_node_index(self, index):

        if index > self.get_length():
            return 'Invalid Index'

        elif index == 1:
            self.head = self.head.next

        else:
            count = 1
            itr = self.head
            while itr and count < index:
                if count == index-1:
                    itr.next = itr.next.next
                count += 1
                itr = itr.next

    def delete_node_value(self, value):
    
        if self.head.data == value:
            if self.head.next == None:
                self.head = None
            else:   self.head = self.head.next
       

        else:
            itr = self.head
            while itr:
                
                if itr.next:
                    if itr.next.data == value:
                        itr.next = itr.next.next
                itr = itr.next

    def insert_after_val(self, value_after, value_insert):
        
        itr = self.head
        flag = True

        while itr:
            if itr.data == value_after:
                flag = False
                tmp = itr.next
                itr.next = Node(value_insert, tmp)
            itr = itr.next
        
        if flag:
            print("Value Not Found")


    def print_linke_list(self):
        if self.head is None:
            print("List is Empty")
            return
        itr = self.head

        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    

if __name__ == '__main__':

    ll = linked_list()
    ll.insert_at_beg(45)
    ll.insert_at_beg(41)
    ll.insert_at_beg(46)
    ll.insert_at_beg(49)
    ll.insert_at_end(12)
    ll.insert_at_end(9)
    ll.insert_at_given_index(2,22)
    ll.insert_at_given_index(5,33)
    
    #ll.insert_values(['ab','as','we','ty','uk','py'])
    ll.print_linke_list()
    print("Lenth of Linked List:",ll.get_length())
    # print(ll.insert_at_given_index(12,11))

    ll.delete_node_index(8)
    print("After Deletion")
    ll.print_linke_list()


    ll.insert_after_val(22,111)
    ll.insert_after_val(45,54)
    ll.insert_after_val(12,154)
    print("After Insertion")
    ll.print_linke_list()


    ll.delete_node_value(22)
    ll.delete_node_value(111)
    ll.delete_node_value(154)
    ll.delete_node_value(49)
    ll.delete_node_value(22)
    ll.delete_node_value(41)
    ll.delete_node_value(46)
    print('After Deletion')
    ll.print_linke_list()
    