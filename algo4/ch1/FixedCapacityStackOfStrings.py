class FixedCapacityStack:
	def __init__(self,n):
		self._theElements = n*[None]
		self._count = 0

	def isEmpty(self):
		return self._count == 0

	def isFull(self):
		return self._count == len(self._theElements)

	def size(self):
		return len(self._theElements)

	def push(self,data):
		if not self.isFull():
			self._theElements[self._count] = data
			self._count += 1

	def pop(self):
		if not self.isEmpty():
			self._count -= 1
			return self._theElements.pop(self._count)

def main():
	stack = FixedCapacityStack(10)
	string = raw_input()
	string = string.split()
	#print string
	for token in string:
		if token is not "-":
			stack.push(token)
		elif not stack.isEmpty():
			print stack.pop()
main()
