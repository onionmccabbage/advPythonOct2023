# we will ask the user for values and use them to create a fugure instance
from my_figures import Figure

def askUser():
    '''CAREFUL - remember every user input returns a string'''
    s = int( float( input('How many sides? ') ) ) # take the int of a float
    z = float( input('What size? ') )
    c = input('What colour? ')
    n = input('Figure name? ')
    sh = Figure(s, z, c, n)
    return sh

if __name__ == '__main__':
    shape = askUser()
    print(shape)
