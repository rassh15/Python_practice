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


    def display_tree(self):
        level = self.tree_level()        

        print(f"{'|__'*level} {self.data}")
        if self.child:
            for child in self.child:
                child.display_tree()



def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Apple'))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("HP"))

    smartphone = TreeNode("Smartphone")
    smartphone.add_child(TreeNode("Samsung"))
    smartphone.add_child(TreeNode("Nokia"))
    smartphone.add_child(TreeNode("Realme"))
    smartphone.add_child(TreeNode("Lenovo"))

    camera = TreeNode("Camera")
    camera.add_child(TreeNode("Nikon"))
    camera.add_child(TreeNode("Canon"))
    camera.add_child(TreeNode("Fuji"))

    root.add_child(laptop)
    root.add_child(smartphone)
    root.add_child(camera)

    
    root.display_tree()


if __name__ == "__main__":
    build_product_tree()
    





    