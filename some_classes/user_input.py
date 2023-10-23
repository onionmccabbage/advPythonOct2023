# we will ask the user for values and use them to create a fugure instance
from my_figures import Figure

def askUser():
    s = input('How many sides? ')
    z = input('What size? ')
    c = input('What colour? ')
    n = input('Figure name? ')
    sh = Figure(s, z, c, n)
    return sh

if __name__ == '__main__':
    shape = askUser()
    print(shape)
