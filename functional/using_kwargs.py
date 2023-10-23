# in addition to a tuple of positional arguments, we can also access any keyword arguments

def doStuff( *args, **kwargs ): # **kwargs will gather all the keyword arguments into a dictionary called kwargs
    '''return the arguments'''
    return args, kwargs


if __name__ == '__main__':
    print( doStuff() ) # no keyword arguments
    print( doStuff(True, x=99) ) # a single keyword argument
    print( doStuff('a', 'b', m=True, n=False) ) # two keyword arguments
    print( doStuff(a='one', b='two', c='three') ) # three keyword arguments