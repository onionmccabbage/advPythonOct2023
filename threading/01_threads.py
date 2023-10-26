# NB we should usually avoid using a digit for the first character of a module name
# we can use letters, numbers and underscore in module names
from threading import Thread

# this time we wil use a function for threading

def myFn():
    '''This is a normal function which can be invoked in the usual way
    Like any function we may choose to invoke it in a new thread (in addition to the main thread)'''
    print('This is my function')

if __name__ == '__main__':
    '''we can target any function to be run as a separate thread'''
    t = Thread(target=myFn) # Thread is a thread-access-object
    t.start() # at this point our function will be exexuted on the new thread
