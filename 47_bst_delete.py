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

    # def find_min(self):
    #     min_val = self.data
    #     if self.left:
    #         return self.left.find_min()

    #     return min_val


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete_node(self, value):

        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)

        else:
            #node has no children and on lead node
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete_node(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_node(max_val)

        return self



    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
        



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

    # print(tree.search_data(29))


    tree.delete_node(8)
    # print(a.data)
    # tree.delete(12)

    print(tree.inorder_traversal())

    

