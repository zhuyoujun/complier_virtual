##https://oj.leetcode.com/problems/same-tree/
##Given two binary trees, write a function to check if they are equal or not.
##Two binary trees are considered equal 
##if they are structurally identical and the nodes have the same value.

class TreeNode:
	def __init__(self,data):
		self.data  = data
		self.left  = None
		self.right = None


def SameTree(root1,root2):

	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> root1 = None
	>>> root2 = None
	>>> SameTree(root1,root2)
	True
	>>> root1 = TreeNode(1)
	>>> SameTree(root1,root2)
	False
	>>> root2 = TreeNode(1)
	>>> SameTree(root1,root2)
	True
	>>> root1.left = TreeNode(2)
	>>> SameTree(root1,root2)
	False
	>>> root2.left = TreeNode(2)
	>>> SameTree(root1,root2)
	True
	>>> root1.right = TreeNode(3)
	>>> SameTree(root1,root2)
	False
	>>> root2.right = TreeNode(3)
	>>> SameTree(root1,root2)
	True
	>>> root1.left.right = TreeNode(4)
	>>> SameTree(root1,root2)
	False
	>>> root2.left.right = TreeNode(4)
	>>> SameTree(root1,root2)
	True
	>>> root1.right.left = TreeNode(5)
	>>> SameTree(root1,root2)
	False
	>>> root2.right.left = TreeNode(5)
	>>> SameTree(root1,root2)
	True
	"""
	if root1 is None and root2 is None:
		return True
	elif root1 is not None and root2 is not None:
		return (root1.data == root2.data) and SameTree(root1.left,root2.left) and SameTree(root1.right,root2.right)
	else:
		return False






