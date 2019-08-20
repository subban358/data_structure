# Lowest Common Ancestor !! dekh bhai
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def findPath(root,path,n):
    
    if root is None:
        return False
    
    if root.value == n:
        return True
    
    if (root.left!=None and findPath(root.left,path,n)) or (root.right!=None and findPath(root.right,path,n)):
        path.insert(0,root.value)
        return True
    
    return False
        
 
def common(l,l1,n1,n2):
    a=None
    
    if n1 in l1:
        return n1
    elif n2 in l:
        return n2
        
    while len(l)!=0 and len(l1)!=0:
        b = l.pop(0)
        c = l1.pop(0)
        if b == c:
            a = b
        else:
            break
    return a    
    
    
def lca(root,node1,node2):
    path1 = []
    path2 = []
    findPath(root,path1,node1)
    findPath(root,path2,node2)
    #print(path1)
    #print(path2)
    return common(path1,path2,node1,node2)
        
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)   

print(lca(root,7,5))

