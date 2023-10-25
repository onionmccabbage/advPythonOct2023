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

def cubeIt(a, b):
    '''
    return all the cubes of numbers from a to b
    >>> cubeIt(3, 8)
    [27, 64, 125, 216, 343]
    >>> cubeIt(1, 101) # doctest:+ELLIPSIS
    [1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a, b):
        answers.append( i**3 )
    return answers

if __name__ == '__main__':
    # result = nthPower(2, 4)
    # print(result)
    doctest.testmod(verbose=True)
    # c = cubeIt(1, 9)
    # print(c)
