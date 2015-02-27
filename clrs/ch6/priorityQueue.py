class PriorityQueue:
	def __init__(self,capicity):
		self._theElements = capicity*[None]
		self._size = 0
	def isEmpty(self):
		return self._size == 0

	def 