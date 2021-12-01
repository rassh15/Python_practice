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


    def display_tree(self, name):
        #level = self.tree_level()
        spaces = ' ' * self.tree_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if name == 'name':
            print(f"{prefix}{self.data[0]}")
        elif name == 'designation':
            print(f"{prefix}{self.data[1]}")
        elif name == 'both':
            print(f"{prefix}{self.data[0]} ({self.data[1]})")
        else:
            print('Wrong Input')
            return


       # print(f"{'|__'*level}{self.data[0]} ({self.data[1]})")
        if self.child:
            for child in self.child:
                child.display_tree(name)



def build_product_tree():
    ceo = TreeNode(['Nilupul', 'CEO'])

    cto = TreeNode(['Chinmay','CTO'])
    infra_man = TreeNode(['Vishwa', 'Infrastructure Manager'])
    cto.add_child(infra_man)
    infra_man.add_child(TreeNode(['Dhaval','Cloud Manager']))
    infra_man.add_child(TreeNode(['Abhijeet','App Manager']))
    app_head = TreeNode(['Aamir','Application Head'])
    cto.add_child(app_head)
    
    hr = TreeNode(['Gels','HR Head'])
    hr.add_child(TreeNode(['Peter','Recruitment Manager']))
    hr.add_child(TreeNode(['Waqas','Policy Manager']))


    ceo.add_child(cto)
    ceo.add_child(hr)

    
    ceo.display_tree('both')


if __name__ == "__main__":
    build_product_tree()
    





    