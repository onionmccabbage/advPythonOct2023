from my_shape import Shape # we an import from our own modules

# Inheritance: any class may inherit everything from another class
class Figure(Shape):
    '''Everything from the Shape class now exists in the Figure class'''
    # Notice - there is no need for any __init__ etc.
    def __init__(self, num_sides, size, colour='black', s_name='shape'):
        super().__init__(num_sides, size, colour) # call the __ini__ of the parent class
        self.s_name = s_name
    @property
    def s_name(self):
        return self.__s_name
    @s_name.setter
    def s_name(self, new_name):
        if isinstance(new_name, str):
            self.__s_name = new_name
        else:
            pass
    # if we like, we could write a new __str__ method just for this class

if __name__ == '__main__':
    fig1 = Figure(colour='pink', num_sides=8, size=0.0000003, s_name='Octagon')
    print(fig1)