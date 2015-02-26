##https://oj.leetcode.com/problems/single-number/
##Given an array of intergers,every element appears twice
##except for one,find that signle one.

def SingleNumber(Array):

	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> Array = []
	>>> SingleNumber(Array)
	0
	>>> Array = [10]
	>>> SingleNumber(Array)
	10
	>>> Array = [1,2,2]
	>>> SingleNumber(Array)
	1
	>>> Array = [1,1,2,2,3,3,4]
	>>> SingleNumber(Array)
	4
	>>> Array = [i for i in range(1000)]*2 +[1000]
	>>> SingleNumber(Array)
	1000
	"""
	result = 0
	for i in range(len(Array)):
		result ^= Array[i]
	return result

def SingleNumberI(Array):
	""" Given an array of intergers,every element appears twice
	except for one,find that signle one.
	>>> Array = []
	>>> SingleNumberI(Array)
	0
	>>> Array = [10]
	>>> SingleNumberI(Array)
	10
	>>> Array = [1,2,2]
	>>> SingleNumberI(Array)
	1
	>>> Array = [1,1,2,2,3,3,4]
	>>> SingleNumberI(Array)
	4
	>>> Array = [i for i in range(1000)]*2 +[1000]
	>>> SingleNumberI(Array)
	1000
	"""
	bit32 = 32*[0]
	for i in range(len(Array)):
		tmp = Array[i]
		for bit in range(32): 
			if tmp != 0:
				bit32[bit] += tmp%2
				tmp = tmp // 2
	result = 0
	for i in range(32):
		result += (bit32[i]%2)*(2**i)
	return result






