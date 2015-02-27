# disc03
def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    if n == 1:
        print(1)
    else:
        print(n)
        countdown(n-1)
    return 


def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """
    if n == 1:
        print(1)
    else:
        countup(n-1)
        print(n)
    return


def expt(base, power):
    """
    >>> expt(2,3)
    8
    >>> expt(2,-3)
    0.125
    >>> expt(0,-3)
    0
    """
    if base == 0:
        return 0
    elif power >= 0:
        return expt_pos(base,power)
    elif power < 0:
        return 1 / expt_pos(base,-power)


def expt_pos(base,power):
    if power == 1:
        return base
    else:
        return base*expt_pos(base,power-1)


