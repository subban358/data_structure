# Python3 program to find the maximum depth of tree 

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def maxDepth(node): 
    if node is None: return 0
    if node:
        return 1+max(maxDepth(node.left), maxDepth(node.right))

def sumofLevel(node,level,l):
    if node == None:
        return
    else:
        l[level] += node.data    

        sumofLevel(node.left,level+1,l)
        sumofLevel(node.right,level+1,l)

if __name__=='__main__':    
    root = Node(5) 
    root.left = Node(8) 
    root.right = Node(7) 
    root.left.left = Node(3) 
    root.left.right = Node(9) 
    root.right.left = Node(2) 
    root.right.right = Node(10) 
    lvl = maxDepth(root)
    l= [0]*lvl
    sumofLevel(root,0,l)
    print(l)
    
