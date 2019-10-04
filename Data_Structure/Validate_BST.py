INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 

class Tree:
    def __init__(self,data):
        self.root = Node(data)
    
    def validate(self,root,mx,mn):
        if root == None:
            return True
        if root.data < mn or root.data > mx:
            return False
        return self.validate(root.left,root.data,mn) and self.validate(root.right,mx,root.data)    


t = Tree(10)
t.root.left = Node(-10)
t.root.right = Node(19)
t.root.left.left = Node(-20)
t.root.left.right = Node(0)
t.root.right.left = Node(17)

print(t.validate(t.root,INT_MAX,INT_MIN))
