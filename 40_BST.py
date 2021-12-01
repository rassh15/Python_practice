class bst():
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

    def add_node(self, data):
        # check for duplicate values
        if self.data == data:
            return

        #check node greater than root node

        if data < self.data:
            #Add node in left sub-tree
            if self.left:
                self.left.add_node(data)
            else:   self.left = bst(data)

        else:
            #Add node in right sub-tree
            if self.right:
                self.right.add_node(data)
            else:   self.right = bst(data)

    def inorder_traversal(self):
        elems = []
        

        #first add left node data
        if self.left:
            elems += self.left.inorder_traversal()

        #second base node data
        elems.append(self.data)

        #third right node data
        if self.right:
            elems += self.right.inorder_traversal()

        print("eleme", elems)

        return elems


    def search_data(self, value):

        if self.data ==value:
            return "Found"
        
        if value < self.data:
                
            if self.left:
                return self.left.search_data(value)
            else:   return "Not Found"   
        
        if value > self.data:
                
            if self.right:
                return self.right.search_data(value)
            else:   return "Not Found"




def build_tree(elements):
    root = bst(elements[0])

    for i in range(1,len(elements)):
        root.add_node(elements[i])

    return root


    

if __name__ == '__main__':
    tree_data = [45,23,12,44,7,8,4,90,65,32]
    print(tree_data)

    tree = build_tree(tree_data)
    print(tree.inorder_traversal())

    print(tree.search_data(29))

    

