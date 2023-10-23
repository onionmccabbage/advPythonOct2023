# we can write methods that belong to the class (rather than belonging to class instances)
class Duck():
    count=0 # this variable is now a property of the Duck class
    def __init__(self, n):
        self.__n = n
        Duck.count += 1
    @classmethod # ensure the method belongs to the class
    def howMany(cls): 
        return f'The Duck class has {cls.count} instances'
    
if __name__ == '__main__':
    d1 = Duck('Howard')
    d2 = Duck('Mallard')
    d3 = Duck('Eider')
    print(Duck.count) # should print 3
    print(Duck.howMany())
