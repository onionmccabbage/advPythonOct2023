from custom_decorator import showArgs

@showArgs
def raisePower(m, n):
    '''raise m to the power of n'''
    return m**n
@showArgs
def squareIt(x):
    '''return the square of a number'''
    return x*x
@showArgs
def addThem(x, y):
    '''return the sum of two numbers'''
    return x+y

if __name__ == '__main__':
    a = addThem(x=2, y=3)
    s = squareIt(9)
    r = raisePower(3, n=2)

    print(a, s, r)