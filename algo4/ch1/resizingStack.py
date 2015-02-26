class ResizingStack:
	def __init__(self):
		self._theElements = 1*[0]
		self._count = 0

	def isEmpty(self):
		return self._count == 0

	def isFull(self):
		return self._count == len(self._theElements)

	def size(self):
		return len(self._theElements)

	def push(self,data):
		self._resize()
		if not self.isFull():
			self._theElements[self._count] = data
			self._count += 1


	def pop(self):
		if not self.isEmpty():
			self._count -= 1
			item = self._theElements.pop(self._count)
			#self._resize()
			return item

	def __str__(self):
		for elem in self._theElements:
			print elem,
		return ''

	def _resize(self):
		length = len(self._theElements)
		if self._count >=length:
			newList = 2*length*[None]
			for i in range(self._count):
				newList[i] = self._theElements[i]
			self._theElements = newList
		elif self._count <= length/4:
			newList = length/2*[None]
			for i in range(self._count):
				newList[i] = self._theElements[i]
			self._theElements = newList			

def main():
	stack = ResizingStack()
	string = raw_input()
	string = string.split()
	for token in string:
		if token is not "-":
			stack.push(token)
		elif not stack.isEmpty():
			print stack.pop()
		print stack
main()
