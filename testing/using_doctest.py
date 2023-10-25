import doctest # we can write unit tests in the dostring

def nthPower(d=2, p=4):
    '''
    return the nth power of a number
    we can write tests within this docstring
    The three chevrons >>> represent python immediate mode
    >>> nthPower(4, 3)
    64
    >>> nthPower()
    16
    '''
    return d**p

if __name__ == '__main__':
    # result = nthPower(2, 4)
    # print(result)
    doctest.testmod(verbose=True)
