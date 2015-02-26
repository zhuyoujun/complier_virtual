##https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
##Given a binary tree, find its maximum depth.
##The maximum depth is the number of nodes along the longest path 
##from the root node down to the farthest leaf node.

class TreeNode:
	def __init__(self,data):
		self.data  = data
		self.left  = None
		self.right = None


def MaxDepthOfBinaryTree(root):

	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> root = None
	>>> MaxDepthOfBinaryTree(root)
	0
	>>> root = TreeNode(1)
	>>> MaxDepthOfBinaryTree(root)
	1
	>>> root.left = TreeNode(2)
	>>> MaxDepthOfBinaryTree(root)
	2
	>>> root.right = TreeNode(3)
	>>> MaxDepthOfBinaryTree(root)
	2
	>>> root.left.right = TreeNode(4)
	>>> MaxDepthOfBinaryTree(root)
	3
	>>> root.right.left = TreeNode(5)
	>>> MaxDepthOfBinaryTree(root)
	3

	"""
	if root is None:
		return 0
	else:
		return 1 + max(MaxDepthOfBinaryTree(root.left),MaxDepthOfBinaryTree(root.right))


def MaxDepthOfBinaryTreeI(root):

	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> root = None
	>>> MaxDepthOfBinaryTreeI(root)
	0
	>>> root = TreeNode(1)
	>>> MaxDepthOfBinaryTreeI(root)
	1
	>>> root.left = TreeNode(2)
	>>> MaxDepthOfBinaryTreeI(root)
	2
	>>> root.right = TreeNode(3)
	>>> MaxDepthOfBinaryTreeI(root)
	2
	>>> root.left.right = TreeNode(4)
	>>> MaxDepthOfBinaryTreeI(root)
	3
	>>> root.right.left = TreeNode(5)
	>>> MaxDepthOfBinaryTreeI(root)
	3

	"""
	if root is None:
		return 0
	queue = list()
	queue.append(root)
	count = 1
	depth = 0
	while len(queue)>0:
		node = queue.pop(0)
		count -= 1
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
		if count == 0:
			depth += 1
			count = len(queue)
	return depth




