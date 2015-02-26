##define the Queue class using linked Node
##the elements enqueue in the tial
##and dequeue from the front

class Queue:
	def __init__(self):
		self._front = None
		self._tail = None
		self._count = 0

	def isEmpty(self):
		return self._count == 0

	def size(self):
		return self._count

	def enqueue(self,data):
		newNode = _ListNode(data)
		if self._front is None:
			self._front = newNode
			self._tail  = newNode
		else:
			self._tail.next = newNode
			self._tail  = newNode
		self._count += 1

	def dequeue(self):
		if not self.isEmpty():
			item = self._front
			if self._front.next is None:
				self._front = self._front.next
				self._tail = None
			else:
				self._front = self._front.next
			self._count -= 1
			return item.data

class _ListNode:
	def __init__(self,data):
		self.data =  data
		self.next = None


def main():
	q = Queue()
	string = raw_input()
	string = string.split()
	#print string
	for token in string:
		if token is not "-":
			q.enqueue(token)
		elif not q.isEmpty():
			print q.dequeue()
main()
