# slots allow us to restrict the arbitrary members added to class instances
class RestrictMembers:
    '''restrict properties to only x, y and z'''
    __slots__ = ('x', 'y', 'z') # declare a tuple of the permitted properties
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == '__main__':
    r = RestrictMembers(3, 2, 1)
    # r.additional = 'here is an arbitrary property'
    # print(r.__dict__) # we can inspect the members currently atached to our class instance
    print(r.__slots__) # __slots__ replaces __dict for class instances
    print(RestrictMembers.__dict__)