# switching context is a common problem in Python
# There is a library that will help
from contextlib import contextmanager
import sys

@contextmanager # make this function behave as a context manager
def outputRedirect(  newOutput ):
    '''redirect any printed output to a different context'''
    old_stdout = sys.stdout # remember the current output stream
    sys.stdout = newOutput  # set the standard output to our new stream
    yield # our function will yield the next available object to be written
    sys.stdout = old_stdout # put thigns back how they were before

if __name__ == '__main__':
    # first we use the current standard output
    sys.stdout.write('The standard output usually sends to the console (just like print)')
    # next we make a new output target
    with open('my_stream.txt', 'a') as fobj: # we now have a file access object
        with outputRedirect(fobj):
            print('this will be written to our text file')
            sys.stdout.write('more text also context-switched')

    print('All context is returned to the original standard output stream')