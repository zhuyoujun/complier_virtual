def main():
	first = ListNode(1)
	second = ListNode(2)
	third = ListNode(3)
	fourth = ListNode(4)

	first.next = second
	second.next = third
	third.next = fourth

	#given the head,delete the last node in the linked list
	curNode = first


def deleteLastNode(head):
	curNode = head
	if curNode is None:
		return None
	elif curNode.next is None:
		return None
	preNode = None


class ListNode:
	def __init__(self,data):
		self.data = data
		self.next = None
