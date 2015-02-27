# Q9
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    grid = m*[0]
    for i in range(m):
        grid[i] = n*[0]
        grid[i][0] = 1
    for j in range(n):
        grid[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[m-1][n-1]

def paths_recu(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths_recu(2, 2)
    2
    >>> paths_recu(5, 7)
    210
    >>> paths_recu(117, 1)
    1
    >>> paths_recu(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths_recu(m, n-1) + paths_recu(m-1, n)


# Q10
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif a > b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)
