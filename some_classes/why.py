# Why use classes
# Only use a class when nothing else will do

flag = True # boolean values are handy
age  = 37 # an integer 
intelligence = 198.999 # also float
print( type(intelligence) )
greet = 'Hello' # text string (a collection of characters)
# other collections
my_tup = (5,4,8,5,2,8,False, 'string', age, greet) # immutable indexed collection
my_list = [5,4,8,5,2,8,False, 'string', age, greet] # mutable indexed collection
my_set = {6, 4, 8, 8, 2, 3, 2} # unique members
my_dictionary = {'name':'Floella', 'hero':True} # not indexed by number
print(my_set)
# data about shapes
t = (3, 4.5, 'red')
l = [5, 2.5, 'blue']
# built-in collections dont allow validation or facets (min/max)
d = {'shape':'hexagon', 'sides':-6, 'size':'really big', 'colour':False}