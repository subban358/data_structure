from queue import Queue
class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		
class BinaryTree:

	def __init__(self,root):
		self.root = Node(root)
	

	def traverse(self,type):

		if type is"preorder":
			print(type+" "+self.preorder_traversal(self.root,""))
			return 

		elif type is"inorder":
			print(type+" "+self.inorder_traversal(self.root,""))
			return 	

		elif type is"postorder":
			print(type+" "+self.postorder_traversal(self.root,""))
			return 		

		elif type is"levelorder":
			print(type+" "+self.levelorder_traversal(self.root))
			return 		
	
		else:
			print(type+" is not available !")
			return

	def preorder_traversal(self,start,traverse):
		'''root->left->right'''
		if start:
			traverse += (str(start.value)+" ")
			traverse = self.preorder_traversal(start.left,traverse)
			traverse = self.preorder_traversal(start.right,traverse) 
		return traverse	
	
	def inorder_traversal(self,start,traverse):
		'''left->root->right'''
		if start:
			traverse = self.inorder_traversal(start.left,traverse)
			traverse += (str(start.value)+" ")
			traverse = self.inorder_traversal(start.right,traverse) 
		return traverse	

	def postorder_traversal(self,start,traverse):
		'''left->right->root'''
		if start:
			traverse = self.postorder_traversal(start.left,traverse)
			traverse = self.postorder_traversal(start.right,traverse)
			traverse += (str(start.value)+" ")
			 
		return traverse		

	def levelorder_traversal(self, start):
		''' level by level '''
		if start:
			q=Queue()
			q.enqueue(start)
			traverse=""
			while len(q)>0:
				traverse += str(q.peek())+" "
				node = q.dequeue()
				if node.left:
					q.enqueue(node.left)
				if node.right:
					q.enqueue(node.right)
		return traverse				


if __name__ == '__main__':
	
	t = BinaryTree(20)
	t.root.left = Node(17)
	t.root.right = Node(23)
	t.root.left.left = Node(10)
	t.root.left.right = Node(19)
	t.root.right.left = Node(21)
		
	t.traverse("preorder")
	t.traverse("inorder")
	t.traverse("postorder")
	t.traverse("levelorder")



