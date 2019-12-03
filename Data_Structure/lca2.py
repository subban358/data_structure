class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

def lca(root, v1, v2):
    if root is None:
        return None 
    if (root.info == v1 or root.info == v2):
        return root   
    left = lca(root.left,v1,v2)
    right = lca(root.right,v1,v2)
    if(left != None and right != None):
        return root
    if(left == None and right == None):
        return None
    if(left != None):
        return left 
    else:
        return right  
