class Node:
	def __init__(self,data):
		self.left=None
		self.data=data
		self.right=None

class BinaryTree:

	def createnode(self,data):
		return Node(data)

	def insert_node(self,node,data):
		if node is None:
			return self.createnode(data)
		if data>node.data:
			node.right=self.insert_node(node.right,data)
		else:
			node.left=self.insert_node(node.left,data)
		return node

	def inorder_traversal(self,node):
		if node:
			self.inorder_traversal(node.left)
			print(root.data)
			self.inorder_traversal(node.right)
		

	def preorder_traversal(self,node):
		if node:
			print(node.data)
			self.preorder_traversal(node.left)
			self.preorder_traversal(node.right)

	def postorder_traversal(self,node):
		if node:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print(node.data)

	def levelorder_traversal(self,root):
		if root is None:
			return 
		q=[]
		q.append(root)
		while len(q)!=0:
			node1=q.pop(0)
			print(node1.data)
			if node1.left is not None:
				q.append(node1.left)
			if node1.right is not None:
				q.append(node1.right) 
		
	def Find_height(self,root):
		if root is None:
			return -1
		h=max(self.Find_height(root.left),self.Find_height(root.right))+1
		return h

//driver code

t=BinaryTree()
root=t.createnode(3)
t.insert_node(root,1)
t.insert_node(root,4)
t.insert_node(root,5)
t.insert_node(root,2)
t.insert_node(root,12)
t.levelorder_traversal(root)
print("height of tree: ",t.Find_height(root))
# t.preorder(root)
# t.postorder(root)