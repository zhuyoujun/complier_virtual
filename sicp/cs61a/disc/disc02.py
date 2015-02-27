##http://www-inst.eecs.berkeley.edu/~cs61a/fa14/disc/disc02.pdf


# It’s lecture time! However, whether you go depends on certain conditions about timing,
# seats, and laziness. Write a simple function which lecture that takes in inputs
# time, seats left, is lazy and prints out your decision.
# 	which lecture should print "go to lecture" if time is before 2:00pm, there
# are seats, and you are not lazy.
# 	which lecture should print "go to alt lecture" if time is after 2:00pm or
# there are no seats, and you are not lazy.
# 	which lecture should print "watch videos" if you feel lazy.
# time is in military format; e.g 2:20pm is 1420. seats left is a non-negative integer.
# is lazy is a boolean variable.

def which_lecture(time, seats_left, is_lazy):
	"""determine whether go to lecture or not.
	>>> time = 1430
	>>> seats_left = 0
	>>> is_lazy = True
	>>> which_lecture(time, seats_left, is_lazy)
	watch videos
	>>> is_lazy = False
	>>> seats_left = 10
	>>> which_lecture(time, seats_left, is_lazy)
	go to alt lecture
	>>> time = 1330
	>>> seats_left = 10
	>>> which_lecture(time, seats_left, is_lazy)	
	go to lecture
	>>> time,seats_left,is_lazy = 1330,10,True
	>>> which_lecture(time, seats_left, is_lazy)

	>>> time,seats_left,is_lazy = 1330,0,False
	>>> which_lecture(time, seats_left, is_lazy)

	>>> time,seats_left,is_lazy = 1430,0,False
	>>> which_lecture(time, seats_left, is_lazy)

	"""
	if is_lazy and seats_left == 0:
		print("watch videos")
	elif not is_lazy and time < 1400 and seats_left > 0:
		print("go to lecture")
	elif not is_lazy and time > 1400 and seats_left > 0:
		print("go to alt lecture")

def is_prime(n):
	"""if n is a prime number,return True,else return False.
	>>> is_prime(2)
	True
	>>> is_prime(3)
	True
	>>> is_prime(4)
	False
	>>> is_prime(5)
	True
	>>> is_prime(14)
	False
	>>> is_prime(17)
	True
	"""
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1
	return True

def choose(n,k):
	"""Returns the number of ways to choose K items from N items.
	>>> choose(5, 2)
	10
	>>> choose(20, 6)
	38760
	"""
	i = n
	j = 1
	result1 = 1
	result2 = 1
	while j <= k:
		result1 *= i
		result2 *= j
		i -= 1
		j += 1
	return result1 // result2

def square(x):
	"""
	>>> square(3)
	9
	>>> square(5)
	25
	"""
	return x * x
def square_every_number(n):
	"""Prints out the square of every integer from 1 to n.
	>>> square_every_number(3)
	1
	4
	9
	"""
	for i in range(1,n+1):
		print(square(i))

def double(x):
	"""
	>>> double(3)
	6
	>>> double(5)
	10
	"""
	return 2 * x
def double_every_number(n):
	"""Prints out the double of every integer from 1 to n.
	>>> double_every_number(3)
	2
	4
	6
	"""
	for i in range(1,n+1):
		print(double(i))

def every(func, n):
	"""Prints out all integers from 1 to n with func applied
	on them.
	>>> def square(x):
	... 	return x * x
	>>> every(square, 3)
	1
	4
	9
	>>> def cube(x):
	... 	return x * x * x
	>>> every(cube, 3)
	1
	8
	27
	"""
	for i in range(1,n+1):
		print(func(i))

def keep(cond, n):
	"""Prints out all integers from 1 to n that return True
	when called with cond.
	>>> def is_even(x):
	... 	# Even numbers have remainder 0 when divided by 2.
	... 	return x % 2 == 0
	>>> keep(is_even, 5)
	2
	4
	>>> def is_odd(x):
	... 	# Odd numbers have remainder 1 when divided by 2.
	... 	return x % 2 == 1
	>>> keep(is_odd, 5)
	1
	3
	5
	"""
	for i in range(1,n+1):
		if cond(i):
			print(i)

def and_add(f, n):
	"""Returns a new function. This new function takes an
	argument
	x and returns f(x) + n.
	>>> def square(x):
	... 	return x * x
	>>> new_square = and_add(square, 3)
	>>> new_square(4) # 4 * 4 + 3
	19
	"""
	def add(x):
		return f(x) + n
	return add


def skipped(f):
	def g():
		return f
	return g
def composed(f, g):
	def h(x):
		return f(g(x))
	return h
def added(f, g):
	def h(x):
		return f(x) + g(x)
	return h
def square(x):
	return x*x
def two(x):
	return 2
##>>> composed(square, two)(7)
##4
##>>> skipped(added(square, two))()(3)
##11
##>>> composed(two, square)(2)
##2