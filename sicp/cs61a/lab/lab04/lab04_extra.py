from lab04 import *

# Q5
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    n = len(lst)
    newLst = n*[None]
    for i in range(n):
        newLst[n-1-i] = lst[i]
    return newLst

def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    if len(lst) == 1:
        return lst
    else:
        return reverse_recursive(lst[1:]) + [lst[0]]

from lab04 import merge
# Q8
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    n = len(seq)
    if  n <= 1:
        return seq
    else:
        mid = n//2
        left = mergesort(seq[:mid])
        right = mergesort(seq[mid:])
        return merge(left,right)

# Q12
def add_matrices(x, y):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    [for rowx,rowy in x,y]
