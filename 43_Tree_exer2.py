#Tree implementation
#General Tree
#Using class

class TreeNode():
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None

    
    def add_child(self, child):
        #here self is instance of class TreeNode
        #self is parent node of child node
        child.parent = self
        self.child.append(child)


    def tree_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        return level


    def display_tree(self, level):
        tree_level = self.tree_level()

        if tree_level > level:
            return
        spaces = ' ' * tree_level * 3
        prefix = spaces + "|__" if self.parent else ""

        print(f"{prefix}{self.data}") 
        if self.child:
            for child in self.child:
                child.display_tree(level)

    
def build_product_tree():
    
    globall = TreeNode('Global')

    india = TreeNode('India')
    gj = TreeNode('Gujarat')
    ka = TreeNode('Karnataka')
    india.add_child(gj)
    ka.add_child(ka)
    gj.add_child(TreeNode('Ahmedabad'))
    gj.add_child(TreeNode('Baroda'))
    ka.add_child(TreeNode('Mysore'))
    ka.add_child(TreeNode('Bangluru'))

    usa = TreeNode('USA')
    new_jer = TreeNode('New Jersey')
    calf = TreeNode('California')
    
    usa.add_child(new_jer)
    usa.add_child(calf)
    new_jer.add_child(TreeNode('Princeton'))
    new_jer.add_child(TreeNode('Trenton'))
    
    calf.add_child(TreeNode('San Francisco'))
    calf.add_child(TreeNode('Mountain View'))
    calf.add_child(TreeNode('Palo Alto'))

    globall.add_child(india)
    globall.add_child(usa)


    
    globall.display_tree(2)


if __name__ == "__main__":
    build_product_tree()
    





    