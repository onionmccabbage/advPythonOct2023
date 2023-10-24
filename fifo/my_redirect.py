import sys # a reference to the operating system in which python is running

# Python will have a standard output stream called sys.stdout
# print(sys.stdout)

# all classes are objects, and every object-type has its own 'intrinsics'
class RedirectOut():
    '''Redirect output to a different stream, then recover the original stream'''
    def __init__(self, new_stdout): # we can pass in whatever output stream we like
        self.stdo = new_stdout
    # every class has an instrinsic __enter__ and __exit__ which we can override
    def __enter__(self):
        '''the __enter__ method is invoked whenever this class or an instance of it is run'''
        self.orig_stdo = sys.stdout # remember the current system standard output
        sys.stdout = self.stdo # now the system standard output points to our new output stream
    def __exit__(self):
        '''The ___exit__ method is invoked when this class (or an instance) finishes running'''
        sys.stdout = self.orig_stdo # recover the original standard output stream

if __name__== '__main__':
    # we can use 'with' as a means to work with a file access object
    with open('my_log.txt', 'a') as fobj:
        r = RedirectOut() # an instance of our class
        with r:
            print('this output will be sent to the text file')
        # when the 'with' ends, r is released
        print('back to the normal standrad output')