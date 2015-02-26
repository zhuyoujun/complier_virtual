from stack import Stack

def binaryOfDigit(value):
	stack = Stack()
	if value == 0:
		print value
		return 
	while value>0:
		stack.push(value%2)
		value /= 2
	while not stack.isEmpty():
		print stack.pop(),
	print ""

def main():
	for i in range(50):
		if i%5 == 0:
			print "i = ",i
			binaryOfDigit(i)
main()
