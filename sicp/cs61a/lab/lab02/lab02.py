## Boolean Operators ##

# Q3
def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x > 0 and y > 0

## if Statements ##

# Q7

# The code below causes an error when it is loaded.  As a result, we
# comment it out so that it doesn't break other questions.

# When you get to this question, uncomment the code below.  This is a
# good time to figure out how to quickly uncomment lines in your text
# editor.

def compare(a, b):
    """Compares if a and b are equal.

    >>> compare(4, 2)
    'not equal'
    >>> compare(4, 4)
    'equal'
    """
    if a == b:
         return 'equal'
    return 'not equal'


## while Loops ##

# Q9
def falling(n, k):
    """
    Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    """
    result = 1
    i = 0
    start = n
    while i < k:
        result *= start
        start -= 1
        i += 1
    return result

## Higher Order Functions ##

# Q12
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    def print_range(m):
        for i in range(m):
            if i%n == 0:
                print "Buzz!"
            else:
                print i
    return print_range
