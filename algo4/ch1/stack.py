class Stack:
	def __init__(self):
		self._head = None
		self._count = 0

	def isEmpty(self):
		return self._count == 0

	def size(self):
		return self._count

	def push(self,data):
		newNode = _ListNode(data)
		if self._head is None:
			self._head = newNode
		else:
			newNode.next = self._head
			self._head = newNode
		self._count += 1

	def pop(self):
		if not self.isEmpty():
			item = self._head
			self._head = self._head.next
			self._count -= 1
			return item.data

    def peek(self):
    	if not self.isEmpty():
			item = self._head
			return item.data

class _ListNode:
	def __init__(self,data):
		self.data =  data
		self.next = None

"""
def main():
	stack = Stack()
	string = raw_input()
	string = string.split()
	#print string
	for token in string:
		if token is not "-":
			stack.push(token)
		elif not stack.isEmpty():
			print stack.pop()
main()
"""