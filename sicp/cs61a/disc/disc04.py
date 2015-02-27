# disc04
from math import sqrt

def make_city(name,lat,lon):
    """
    >>> make_city('Berkeley', 122, 37)
    ['Berkeley', 122, 37]
    """
    return [name,lat,lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 122, 37)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 122, 37)
    >>> get_lat(city)
    122
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 122, 37)
    >>> get_lon(city)
    37
    """
    return city[2]

def distance(city1, city2):
    """
    >>> city1 = make_city('Berkeley', 122, 37)
    >>> city2 = make_city('MIT', 125, 41)
    >>> distance(city1, city2)
    5.0
    """
    lat1, lon1 = get_lat(city1), get_lon(city1)
    lat2, lon2 = get_lat(city2), get_lon(city2)

    return sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def closet_city(lat,lon,city1,city2):
    """
    >>> lat = 120
    >>> lon = 35
    >>> city1 = make_city('Berkeley', 122, 37)
    >>> city2 = make_city('MIT', 125, 41)
    >>> closet_city(lat,lon,city1,city2)
    'Berkeley'
    """
    city = make_city("default",lat,lon)
    d1 = distance(city,city1)
    d2 = distance(city,city1)
    if d1 > d2:
        return get_name(city2)
    else:
        return get_name(city1)

from fractions import gcd
def rational(n,d):
    """
    >>> rational(2,3)
    [2, 3]
    >>> rational(4,6)
    [2, 3]
    """
    assert d !=0,"denom can not be zero."
    g = gcd(n,d)
    return [n//g,d//g]

def number(x):
    """
    >>> x = rational(2,3)
    >>> number(x)
    2
    >>> x = rational(4,6)
    >>> number(x)
    2
    """
    return x[0]

def denom(x):
    """
    >>> x = rational(2,3)
    >>> denom(x)
    3
    >>> x = rational(4,6)
    >>> denom(x)
    3
    """
    return x[1]

def add_rationals(x,y):
    """
    >>> x = rational(2,3)
    >>> y = rational(4,6)
    >>> add_rationals(x,y)
    [4, 3]
    >>> y = rational(1,3)
    >>> add_rationals(x,y)
    [1, 1]
    """   
    nx,dx = number(x),denom(x)
    ny,dy = number(y),denom(y)
    return rational(nx*dy + ny*dx,dx*dy)

def mul_rationals(x,y):
    """
    >>> x = rational(2,3)
    >>> y = rational(4,6)
    >>> mul_rationals(x,y)
    [4, 9]
    >>> y = rational(1,3)
    >>> mul_rationals(x,y)
    [2, 9]
    """   
    nx,dx = number(x),denom(x)
    ny,dy = number(y),denom(y)
    return rational(nx*ny,dx*dy)

def rationals_are_equal(x,y):
    """
    >>> x = rational(2,3)
    >>> y = rational(4,6)
    >>> rationals_are_equal(x,y)
    True
    >>> y = rational(1,3)
    >>> rationals_are_equal(x,y)
    False
    """   
    nx,dx = number(x),denom(x)
    ny,dy = number(y),denom(y)
    return (nx*dy == dx*ny)

from math import pow
def rational_pow(x, e):
    """
    >>> x = rational(2,3)
    >>> rational_pow(x,2)
    [4, 9]
    >>> rational_pow(x,1)
    [2, 3]
    """
    nx,dx = number(x),denom(x)
    px,py = int(pow(nx,e)),int(pow(dx,e))
    return rational(px,py)







