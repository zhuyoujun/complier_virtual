##https://oj.leetcode.com/problems/majority-element/
##Given an array of size n, find the majority element. 
##The majority element is the element that appears more than n/2 times.
##You may assume that the array is non-empty and the majority element always exist in the array.

def MajorityElement(num):

	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> num = [1]
	>>> MajorityElement(num)
	1
	>>> num = [1,1,2]
	>>> MajorityElement(num)
	1
	>>> num = [2,1,2]
	>>> MajorityElement(num)
	2
	>>> num = [2,1,2,3,3,3,3]
	>>> MajorityElement(num)
	3
	>>> num = 100*[100] + [i for i in range(99)]
	>>> MajorityElement(num)
	100
	"""
	#time complexity is O(NlogN) if the sort method's complexity is O(NlogN)
	num.sort()
	return num[len(num)//2]

def MajorityElement(num):

	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> num = [1]
	>>> MajorityElement(num)
	1
	>>> num = [1,1,2]
	>>> MajorityElement(num)
	1
	>>> num = [2,1,2]
	>>> MajorityElement(num)
	2
	>>> num = [2,1,2,3,3,3,3]
	>>> MajorityElement(num)
	3
	>>> num = 100*[100] + [i for i in range(99)]
	>>> MajorityElement(num)
	100
	"""
	#time complexity is O(N)
	top = num[0]
	count = 0
	for i in range(len(num)):
		if count == 0:
			top = num[i]
			count = 1
		else:
			if top == num[i]:
				count += 1
			else:
				count -= 1
	return top








