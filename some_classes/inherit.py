# in Python EVERYTHING is an Object
# By default classes inherit from object
class A: # this class implicilty inherits from object
    pass

class B(): # this class also implicitly inherits from object
    pass

class C(object): # this clas explicitly inherits from object
    pass

class D(dict): # here we choose to inherit from the tuple class (which inherits from object)
    pass

# usually we place all imports at the top
from abc import ABCMeta, abstractmethod # Abstract Base Class (ABC)

# we may now declare our own abstract classes
class AbstractShape(ABCMeta): # this is now our own abstract class
    '''Abstract means we can declare properties and methods we need in concrete
    without actually writing any implementations'''
    @abstractmethod
    def __str__(self):
        '''we will definitely need a __str__ method in our concrete classes'''
    @property # we can insist that all derived classes have a property like this
    @abstractmethod
    def shape_name(self, new_name):
        pass # we do NOTHING in the abstract

# now we can make some concrete classes which inherit from our abstract base class
# NB usually the ABC would be in a separate module which we would import for use
class S(AbstractShape):
    def __init__(self, name):
        self.shape_name = name
    def __str__(self):
        # here we write an implementation of the method
        return(f'This shape is called {self.shape_name}')
    @property # we satistfy the abstract base class by implementing the concrete properties and methods
    def shape_name(self):
        return self.__shape_name
    @shape_name.getter
    def shape_name(self, new_name):
        if isinstance(new_name, str) and new_name !='':
            self.__shape_name = new_name
        else:
            raise Exception('Shape name must be a non-empty string')
