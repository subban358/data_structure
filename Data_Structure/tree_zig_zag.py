class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data  
def hasNode(lis):
    if len(lis) is 0:
        return False
    return True

def zigzag(root):
    s1 = []
    s2 = []
    s1.append(root)

    while(hasNode(s1) or hasNode(s2)):

        while(hasNode(s1)):
            p1 = s1.pop(-1)
            print(p1.data,end=" ")
            if(p1.right != None):
                s2.append(p1.right)
            if(p1.left != None):
                s2.append(p1.left)
            

        while(hasNode(s2)):
            p = s2.pop(-1)
            print(p.data,end=" ")
            if(p.left != None):
                s1.append(p.left)
            if(p.right != None):
                s1.append(p.right)
            

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
zigzag(root)
            
            