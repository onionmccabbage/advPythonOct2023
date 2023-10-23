# we have met some built in decorators
# @property, @class_method, @abstractmethod ...

def showArgs(f): # here we expect f to be a function (an object)
    '''This function will be used as a decorator for other functions
    It will reveal all the positional and keyword arguments of the decorated function'''
    def newFunc(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'The positional arguments are {args}')
        print(f'The keyword arguments are {kwargs}')
        # we must return the results of calling the original function
        return f(*args, **kwargs)
    return newFunc # return our new function WITHOUT calling it

@showArgs # use the '@' to apply our function as a decorator
def isOdd(n):
    return n%2 ==1

if __name__ == '__main__':
    isOdd(3)
    isOdd(n=3)

