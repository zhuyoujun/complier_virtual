#Count Sort
def CountSort(tobeSortedList,SortedList,k):
	"""
	>>> n = 8
	>>> k = 5
	>>> tobeSortedList = [2,5,3,0,2,3,0,3]
	>>> SortedList = 8*[None]
	>>> CountSort(tobeSortedList,SortedList,k)
	>>> SortedList == [0,0,2,2,3,3,3,5]
	True
	>>> tobeSortedList = [2,5,4,0,2,3,0,3]
	>>> SortedList = 8*[None]
	>>> CountSort(tobeSortedList,SortedList,k)
	>>> SortedList == [0,0,2,2,3,3,4,5]
	True
	>>> tobeSortedList = [2,2,4,0,2,3,0,3]
	>>> SortedList = 8*[None]
	>>> CountSort(tobeSortedList,SortedList,4)
	>>> SortedList == [0,0,2,2,2,3,3,4]
	True
	"""
	count = (k+1)*[0]
	for elem in tobeSortedList:
		count[elem] += 1
	for i in range(1,len(count)):
		count[i] = count[i] + count[i-1]
	for i in range(len(SortedList)-1,-1,-1):
		SortedList[count[tobeSortedList[i]]-1] = tobeSortedList[i]
		count[tobeSortedList[i]] -= 1



