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

#########################
#                       #
#     fractions         #
#                       #
#########################


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

def factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1 
    else:
        return n * factorial(n - 1)

def approx_e(iter=100):
    """
    >>> approx_e()
    2.718281828459045
    >>> approx_e(10)
    2.7182815255731922
    >>> approx_e(0)
    0.0
    >>> approx_e(50)
    2.718281828459045
    """
    e = rational(0,1)
    for i in range(iter):
        fact_i = rational(1,factorial(i))
        e = add_rationals(e,fact_i)
    return number(e)/denom(e)

def inverse_rational(x):
    """Returns the inverse of the given non-zero rational
    number
    >>> x = rational(2,3)
    >>> inverse_rational(x) == rational(3,2)
    True
    >>> x = rational(1,3)
    >>> inverse_rational(x) == rational(3,1)
    True
    """
    nx, dx = number(x), denom(x)
    assert nx != 0,"can no be zero."
    return rational(dx,nx)

def div_rationals(x, y):
    """Returns x / y for given rational x and non-zero
    rational y
    >>> x = rational(2,3)
    >>> y = rational(1,3)
    >>> div_rationals(x, y) == rational(2,1)
    True
    """
    assert number(x) !=0,"the second argument y can no be zero."
    inve_y = inverse_rational(y)
    return mul_rationals(x,inve_y)



#########################
def make_unit(catchphrase, damage):
    """Each unit will have a string catchphrase 
    and an integer amount of damage.
    >>> make_unit('This is Jimmy.', 18)
    ['This is Jimmy.', 18]
    """
    return [catchphrase,damage]

def get_catchphrase(unit):
    """Return the catchphrase element.
    >>> unit = make_unit('This is Jimmy.', 18)
    >>> get_catchphrase(unit)
    'This is Jimmy.'
    """
    return unit[0]

def get_damage(unit):
    """Return the catchphrase element.
    >>> unit = make_unit('This is Jimmy.', 18)
    >>> get_damage(unit)
    18
    """
    return unit[1]

def battle(first, second):
    """Simulates a battle between the first and second unit
    >>> zealot = make_unit('My life for Aiur!', 16)
    >>> zergling = make_unit('GRAAHHH!', 5)
    >>> winner = battle(zergling, zealot)
    GRAAHHH!
    My life for Aiur!
    >>> winner is zealot
    True
    """
    first_catchphrase = get_catchphrase(first)
    second_catchphrase = get_catchphrase(second)
    first_damage = get_damage(first)
    second_damage = get_damage(second)    
    if first_damage < second_damage:
        print(first_catchphrase)
        print(second_catchphrase)
        return second
    else:
        print(second_catchphrase)        
        print(first_catchphrase)
        return first


def make_resource_bundle(minerals, gas):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return minerals
        else:
            return gas
    return get

def select(bundle,i):
    """Return the ith element in bundle."""
    return bundle(i)

def get_minerals(bundle):
    """Return the 0th element in bundle."""
    return select(bundle,0)

def get_gas(bundle):
    """Return the 1th element in bundle."""
    return select(bundle,1)


def make_building(unit, bundle):
    def get(index):
        if index == 0:
            return unit
        else:
            return bundle
    return get

def select(building,i):
    """Return the ith element in building."""
    return building(i)

def get_unit(building):
    return select(building,0)

def get_bundle(building):
    return select(building,1)

def build_unit(building, bundle):
    """Constructs a unit if given the minimum amount of
    resources.
    Otherwise, prints an error message
    >>> barracks = make_building(make_unit('Go go go!', 6),make_resource_bundle(50, 10))
    >>> marine = build_unit(barracks, make_resource_bundle(20,20))
    We require more minerals!
    >>> marine = build_unit(barracks, make_resource_bundle(50,5))
    We require more vespenegas!
    >>> marine = build_unit(barracks, make_resource_bundle(40,5))
    We require more minerals and vespenegas!
    >>> marine = build_unit(barracks, make_resource_bundle(50,10))
    >>> print(get_catchphrase(marine))
    Go go go!
    """
    bundle_minerals   = get_minerals(bundle)
    bundle_gas        = get_gas(bundle)
    building_minerals = get_minerals(get_bundle(building))
    building_gas      = get_gas(get_bundle(building))
    if building_gas <= bundle_gas and building_minerals <= bundle_minerals:
        return get_unit(building)
    elif building_gas <= bundle_gas:
        print("We require more minerals!")
    elif building_minerals <= bundle_minerals:
        print("We require more vespenegas!")
    else:
        print("We require more minerals and vespenegas!")

