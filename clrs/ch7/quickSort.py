def quickSort(Array,left,right):
	"""
	>>> Array = [9,8,7,6,5,4,3,2,1]
	>>> quickSort(Array,0,8)
	>>> Array == [i for i in range(1,10)]
	True
	"""
	if right > left:
		pivot = partition(Array,left,right)
		quickSort(Array,left,pivot-1)
		quickSort(Array,pivot+1,right)

def partition(Array,left,right):
	"""
	>>> Array = [9,8,7,6,5,4,3,2,1]
	>>> partition(Array,0,8)
	8
	>>> Array == [1,8,7,6,5,4,3,2,9]
	True
	>>> Array = [5,8,7,6,9,4,3,2,1]
	>>> partition(Array,0,8)
	4
	>>> Array == [4,1,2,3,5,9,6,7,8]
	True
	>>> Array = [7,5]
	>>> partition(Array,0,1)
	1
	>>> Array == [5,7]
	True
	>>> Array = [5,7]
	>>> partition(Array,0,1)
	0
	>>> Array == [5,7]
	True
	"""	
	pivot = left
	i = left + 1
	j = right
	while i <= j and j >= left:
		if Array[i] > Array[pivot] and Array[j] < Array[pivot]:
			Array[j],Array[i] = Array[i],Array[j]
			i += 1
			j -= 1
		elif Array[i] > Array[pivot]:
			j -= 1
		elif Array[j] < Array[pivot]:
			i += 1
		else:
			i += 1
			j -= 1
	Array[pivot],Array[i-1] = Array[i-1],Array[pivot]
	return i-1

def partitionI(Array,left,right):
	"""
	>>> Array = [9,8,7,6,5,4,3,2,1]
	>>> partitionI(Array,0,8)
	0
	>>> Array == [1,8,7,6,5,4,3,2,9]
	True
	>>> Array = [5,8,7,6,9,4,3,2,1]
	>>> partitionI(Array,0,8)
	0
	>>> Array == [1,8,7,6,9,4,3,2,5]
	True
	>>> Array = [1,8,7,6,9,4,3,2,5]
	>>> partitionI(Array,0,8)
	4
	>>> Array == [1,4,3,2,5,8,7,6,9]
	True
	>>> Array = [7,5]
	>>> partitionI(Array,0,1)
	0
	>>> Array == [5,7]
	True
	>>> Array = [5,7]
	>>> partitionI(Array,0,1)
	1
	>>> Array == [5,7]
	True
	>>> Array = [13,19,9,5,2,8,7,4,21,2,6,11]
	>>> partitionI(Array,0,11)
	8
	>>> Array == [9,5,2,8,7,4,2,6,11,13,19,21]
	True
	"""	
	pivot = right
	i = left - 1
	for j in range(left,right):
		if Array[j] < Array[pivot]:
			i += 1
			Array[j],Array[i] = Array[i],Array[j]
	Array[pivot],Array[i+1] = Array[i+1],Array[pivot]
	return i+1