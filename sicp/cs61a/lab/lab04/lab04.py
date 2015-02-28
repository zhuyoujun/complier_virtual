def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

# Q6
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    deep = 0
    for elem in lst:
        if type(elem) != list:
            deep += 1
        else:
            deep += deep_len(elem)
    return deep


# Q7
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    elif lst1[0] <=lst2[0] and len(lst1) == 1:
        temp = [lst1[0]]
        temp.extend(lst2)
        return temp
    elif lst1[0] >lst2[0] and len(lst2) == 1:
        temp = [lst2[0]]
        temp.extend(lst1)
        return temp
    elif lst1[0] <=lst2[0]:
        temp = [lst1[0]]
        temp.extend(merge(lst1[1:], lst2))
        return temp
    elif lst1[0] >lst2[0]:
        temp = [lst2[0]]
        temp.extend(merge(lst1, lst2[1:]))
        return temp

# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    return [[elem,fn(elem)] for elem in seq if fn(elem)<=upper and fn(elem)>=lower]

# Q13
def deck():
    "*** YOUR CODE HERE ***"

def sort_deck(deck):
    "*** YOUR CODE HERE ***"
