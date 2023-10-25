# here is a class representing a point in 2-d space
class Point(object):
    '''
    class representing x y values of a point'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==int:
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def yx(self, new_y):
        if type(new_y)==int:
            self.__y = new_y
        else:
            raise TypeError


# we can write unittest to test the capabilities of our class