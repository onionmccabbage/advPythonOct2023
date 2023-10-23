import functools

# if all you need to do is carry out some operation, then just (re)use a function

def isOdd(n):
    '''return True if n is odd, False if not'''
    # we ought to validate that n is an integer...
    return n%2 != 0

def addThem(m,n):
    return m+n

if __name__ == '__main__':
    print( isOdd(3) ) # True
    print( isOdd(8) ) # False
    # we can use the function in many ways...
    results = map(isOdd, range(0, 11))
    # we can access each member of the map object
    print( results.__next__() ) # False
    print( results.__next__() ) # True
    print( results.__next__() ) # False
    print( results.__next__() ) # True

    # this next tuple uses only the remaining values
    results_t = tuple( results )
    print(results_t)

    # there is also a 'filter' available
    odds = filter(isOdd, range(-7, 8))
    print( odds.__next__() ) # -7
    # we can use the remaining values to populate a list or a tuple
    odds_l = list(odds)
    print( odds_l )

    # the functools includes a 'reduce' method to iteratively apply a function
    more_odds = filter(isOdd, range(0, 101, 3)) # start, stop-before, step
    r = functools.reduce( addThem, more_odds )
    print(r)

    # we may need to work with extremely large ranges or even never ending series of values
    big = filter( isOdd, range(-10**10, 10**10) )
    print(big) # we have a generator. At no time to all the values persist in memory
