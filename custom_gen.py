def demo():
    # generators are a part of python
    r = range(1, 99, 7) # start, stop-before, step
    o = (n for n in range(1, 99, 2))
    # we can always iterate over a generator
    for i in o:
        print(i, end=', ')
    # the benefit of generators is that at no time do the values all exist in memory
    # the values are generated on demand from a range or a generator object

def my_gen():
    '''generate never ending exponential values and yield the results'''
    n=1
    while True: # careful - this is an endless loop
        exp = n*n
        n+=1
        yield exp # the yield statement makes this function a generator

if __name__ == '__main__':
    # demo()
    g = my_gen()
    print(type(g)) # we have a generator
    print( g.__next__() ) # 1
    print( g.__next__() ) # 4
    print( g.__next__() ) # 9
    # we can choose to iterate and use our generator
    for i in range(1, 25):
        print( g.__next__() )
        
