class TopLevel():
    def __str__(self):
        '''Every class will have intrinsics
        __name__ is always the class name'''
        return (TopLevel.__name__)
    
class Derived(TopLevel):
    '''this class inherits from TopLevel'''


if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    # we can see any of the intrinsic members of a class
    print( TopLevel.__name__ ) # always the name of the class
    print( Derived.__name__ )
    print( TopLevel.__bases__ ) # always the bases from which it inherits
    print( Derived.__bases__ )
    print( Derived.__doc__ ) # always the docstring