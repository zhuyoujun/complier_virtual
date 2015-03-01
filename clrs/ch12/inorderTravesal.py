##Implent the inorder Travesal function using stack.
class TreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def inorderTravesal(root):
	"""	
	"""
	stack = list()
	if root is None:
		return
	treeNode = root
	while True:
		if treeNode.left is None and treeNode.right is None:
			print(treeNode.data)
			if len(stack)!=0:
				treeNode = stack.pop()
				print(treeNode.data)
				treeNode = treeNode.right
			else:
				break
		elif treeNode.left is not None:
			stack.append(treeNode)
			treeNode = treeNode.left
def search_iter(root,key):
	node = root
	while node is not None and node.data != key:
		if key < node.data:
			node = node.left
		else:
			node = node.right
	return node

def search(root,key):
	if root is None:
		return
	elif key == root.data:
		return root
	elif key < root.data:
		return search(root.left,key)
	elif key > root.data:
		return search(root.right,key)

def maxium(root):
	if root is None:
		return
	elif root.right is None:
		return root.data
	else:
		return maxium(root.right)

def minium(root):
	node = root
	if node is None:
		return
	while node.left is not None:
		node = node.left
	return node.data

def insert(root,data):
	if root is None:
		root = TreeNode(data)
	elif root.data < data:
		root.right = insert(root.right,data)
	else:
		root.left = insert(root.left,data)
	return root




def main():
#   10
#  4   17
# 1 5 16 21
	node21   = TreeNode(21)
	node17 = TreeNode(17)
	node16 = TreeNode(16)
	node10 = TreeNode(10)
	node5  = TreeNode(5)
	node4  = TreeNode(4)
	node1  = TreeNode(1)
	root = node10
	root.left  = node4
	root.right = node17
	node4.left  = node1
	node4.right = node5
	node17.left  = node16
	node17.right = node21
	inorderTravesal(root)
	key = 16
	node = search_iter(root,key)
	print("key = ",node.data)
	key = 5
	node = search_iter(root,key)
	print("key = ",node.data)
	key = 16
	node = search(root,key)
	print("key = ",node.data)
	key = 5
	node = search(root,key)
	print("key = ",node.data)

	maxData = maxium(root)
	print(maxData)
	minData = minium(root)
	print(minData)

	root = insert(root,2)
	print('root = ',root.data)
	inorderTravesal(root)
main()
