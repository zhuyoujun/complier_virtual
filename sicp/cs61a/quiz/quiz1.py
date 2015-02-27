# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    if a == b and b != c:
        return True
    elif b == c and c != a:
        return True
    elif c == a and a != b:
        return True
    else:
        return False



def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    def hailstone(n):
        seq = []
        start = n
        while start >= 1:
            if start == 1:
                seq.append(start)
                break
            elif start%2 == 0:
                seq.append(start)
                start = start // 2
            elif start % 2 != 0:
                seq.append(start)
                start = start * 3 + 1
        return seq
    return (a in hailstone(b)) or  (b in hailstone(a))           

def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    height = 1
    while height < perimeter/2:
        width = perimeter/2 - height
        if abs(height/width - width/height + 1) < 0.02:
            return height
        height += 1cd
        




