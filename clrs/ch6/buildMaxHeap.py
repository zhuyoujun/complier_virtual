from maxHeapify import maxHeapify
def buildMaxHeap(Array):
	""" Build the max heap.
	>>> Array = [9,8,7,6,5,4,3,2,1]
	>>> buildMaxHeap(Array)
	>>> Array == [9,8,7,6,5,4,3,2,1]
	True
	>>> Array = [9,8,7,6,5,4,3,2,7]
	>>> buildMaxHeap(Array)
	>>> Array == [9,8,7,7,5,4,3,2,6]
	True
	>>> Array = [9,8,7,6,5,4,3,2,1,10]
	>>> buildMaxHeap(Array)
	>>> Array == [10,9,7,6,8,4,3,2,1,5]
	True
	>>> Array = [4,1,3,2,16,9,10,14,8,7]
	>>> buildMaxHeap(Array)
	>>> Array == [16,14,10,8,7,9,3,2,4,1]
	True
	"""
	n = len(Array)//2
	size = len(Array)
	while n >= 0:
		maxHeapify(Array,n,size)
		n -= 1

def heapSort(Array):
	"""
	>>> Array = [9,8,7,6,5,4,3,2,1]
	>>> heapSort(Array)
	>>> Array == [i for i in range(1,10)]
	True
	>>> Array = [9,8,7,6,5,4,3,2,7]
	>>> heapSort(Array)
	>>> Array == [2,3,4,5,6,7,7,8,9]
	True
	>>> Array = [9,8,7,6,5,4,3,2,1,10]
	>>> heapSort(Array)
	>>> Array == [i for i in range(1,11)]
	True
	>>> Array = [4,1,3,2,16,9,10,14,8,7]
	>>> heapSort(Array)
	>>> Array ==[1,2,3,4,7,8,9,10,14,16]
	True
	"""
	buildMaxHeap(Array)
	n = len(Array)-1
	size = len(Array)
	while n >= 1:
		Array[n],Array[0] = Array[0],Array[n]
		size -= 1
		maxHeapify(Array,0,size)
		n -= 1
		print(Array)



    

