def minHeapify(Array,i):
	""" Matain the max heap property.
	>>> Array = [1,5,8,3,7,9,10]
	>>> minHeapify(Array,1)
	>>> Array == [1,3,8,5,7,9,10]
	True
	>>> Array = [6,5,8,3,7,9,10]
	>>> minHeapify(Array,0)
	>>> Array == [5,3,8,6,7,9,10]
	True
	"""
	left = 2*i + 1
	right = 2*i + 2
	largest = i
	if left < len(Array) and Array[left] < Array[i]:
		largest = left
	if right < len(Array) and Array[right] < Array[largest]:
		largest = right
	if largest !=i:
		Array[largest],Array[i] = Array[i],Array[largest]
		minHeapify(Array,largest)
