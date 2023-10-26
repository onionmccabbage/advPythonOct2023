# NB we should usually avoid using a digit for the first character of a module name
# we can use letters, numbers and underscore in module names
from threading import Thread
import time
import random
# this time we wil use a function for threading

def myFn(n):
    '''This is a normal function which can be invoked in the usual way
    Like any function we may choose to invoke it in a new thread (in addition to the main thread)'''
    time.sleep( random.random()*2 ) # sleep for up to 2 seconds
    print(f'This is function {n}')

if __name__ == '__main__':
    '''we can target any function to be run as a separate thread'''
    # arguments are passed to threaded functions as a tuple
    t1 = Thread(target=myFn, args=(1,)) # Thread is a thread-access-object
    t2 = Thread(target=myFn, args=(2,)) # Thread is a thread-access-object
    t1.start() # at this point our function will be exexuted on the new thread
    t2.start() # threads are non-blocking (unless they need i/o)
    # we usually choose to join our threads back to the main thread as early as possible
    # t1.join() # if we use join, the main thread will not continue until the thread joins back
    t2.join()
    print('this is on the main thread')
