# we would use a class in order to implement validation on our collection of data

class Shape(): # by convention we use Intiial Cap for class name
    """it is common practice to document classes with a doc string
    triple single quotes or tripple double quotes are fine
    This allows several lines within one string
    This class will capture the number of sides, the size and colour of a shape"""
    def __init__(self, num_sides, size, colour='grey'): # we can choose to supply default values
        '''The __init__ method is similar to a constructor
        it will run once every time we create an instance of this class'''
        self.sides = num_sides
        self.size  = size
        # this will call the colour setter method
        self.colour = colour # we 'mangle' the internal property
    @property # this makes the function behave like a property
    def colour(self):
        return self.__colour
    @colour.setter # now we have a getter and a setter
    def colour(self, new_colour):
        # we can validate the colour
        if isinstance(new_colour, str):
            self.__colour = new_colour
        else: # we could set a default, do nothing or raise an exception
            self.__colour = 'grey'
    @property
    def sides(self):
        return self.__sides
    @sides.setter
    def sides(self, new_sides):
        '''sides cannot be negative or zero and must be an integer'''
        if type(new_sides)==int and new_sides > 0:
            self.__sides = new_sides
        else:
            raise Exception('Number of sides must be a positive integer')
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, new_size):
        '''size must be a positive number (int or float)'''
        if type(new_size)==int or type(new_size)==float:
            self.__size = abs(new_size) # abs ignores any negative sign
        else:
            pass # we might choose to do nothing
    # we can choose to override the built-in mechanism for printing
    def __str__(self):
        '''The __str__ method will always be used when printing this class'''
        return f'This shape has {self.sides} sides and is {self.colour}'

if __name__ == '__main__':
    # .....
    print(Shape.__doc__)
    square = Shape(4, -2.3, [4,3,2]) # this is an instance of our class
    print(square.colour, square.size)
    # we can print our class isntance
    print( square ) # print will call either the default __str__ method or our overriden version
    triangle = Shape(3, 6, 'blue')
    hexagon  = Shape(6, 10, 'purple')
    print(triangle, hexagon)