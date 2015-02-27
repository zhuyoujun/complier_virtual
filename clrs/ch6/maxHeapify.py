def maxHeapify(Array,i,size):
	""" Matain the max heap property.
	>>> Array = [16,4,10,14,7,9,3,2,8,1]
	>>> size = len(Array)
	>>> maxHeapify(Array,1,size)
	>>> Array == [16,14,10,8,7,9,3,2,4,1]
	True
	>>> Array = [16,14,10,4,7,9,3,2,8,1]
	>>> size = len(Array)
	>>> maxHeapify(Array,3,size)
	>>> Array == [16,14,10,8,7,9,3,2,4,1]
	True
	>>> Array = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
	>>> size = len(Array)
	>>> maxHeapify(Array,2,size)
	>>> Array == [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]
	True
	"""
	left = 2*i + 1
	right = 2*i + 2
	largest = i
	if left < size and Array[left] > Array[i]:
		largest = left
	if right < size and Array[right] > Array[largest]:
		largest = right
	if largest !=i:
		maxHeapify(Array,largest,size)

def maxHeapify_iter(Array,i):
	""" Matain the max heap property.
	>>> Array = [16,4,10,14,7,9,3,2,8,1]
	>>> maxHeapify_iter(Array,1)
	>>> Array == [16,14,10,8,7,9,3,2,4,1]
	True
	>>> Array = [16,14,10,4,7,9,3,2,8,1]
	>>> maxHeapify_iter(Array,3)
	>>> Array == [16,14,10,8,7,9,3,2,4,1]
	True
	>>> Array = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
	>>> maxHeapify_iter(Array,2)
	>>> Array == [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]
	True
	"""
	while i < len(Array)/2 + 1:
		left = 2*i + 1
		right = 2*i + 2
		largest = i
		if left < len(Array) and Array[left] > Array[i]:
			largest = left
		if right < len(Array) and Array[right] > Array[largest]:
			largest = right
		if largest !=i:
			Array[largest],Array[i] = Array[i],Array[largest]
			i = largest
		else:
			break