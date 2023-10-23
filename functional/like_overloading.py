# other languages allow several functions with the same name and different signatures
# Python does NOT offer this
def likeOverloading(*args): # the asterisk means all the positional arguments will be gathered into a tuple called 'args'
    if len(args)==0: # we have no positional arguments
        return f'There are no arguments provided'
    if len(args)==1: # we have a single positional argument
        return f'There is one positional argument: {args[0]}'
    if len(args)==2:
        return f'The positional arguments are {args[0]} and {args[1]}'

if __name__ == '__main__':
    # call a fn with no args
    print( likeOverloading() )

    # call a fn with one arg
    print( likeOverloading('a') )

    # call a fn with two args
    print( likeOverloading(True, 0) )