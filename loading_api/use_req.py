import requests

# the 'requests' library may need to be added to python
# pip install requests
# pip3 install requests
# python -m pip install requests

# in earlier python the urllib3 was widely used. The requests library is much more elegant

def getData():
    '''fetch some data from an external API'''
    apiURL = 'https://jsonplaceholder.typicode.com/photos' # this returns data as JSON
    res = requests.get(apiURL) # this is a <response> object
    # this response object will include any JSON data
    res_j = res.json() # or res.text() res.html() res.xml
    return res_j # NB res.json() will convert the JSON into a Python structure

def getOnePhoto(n): # we ought to validate n as a number 1-5000
    '''fetch data representing a single photo'''
    apiURL = 'https://jsonplaceholder.typicode.com/photos' # this returns data as JSON
    res = requests.get( f'{apiURL}/{n}' )
    return res.json() # ...this will be a python structure

if __name__ == '__main__':
    # j = getData() # we now have a list of dict
    # print( type(j[42]) ) # dict
    # ask the user for a number (remember Input ALWAYS returns a string)
    n = input('Which photo (1-5000)? ')
    p = getOnePhoto(n)
    print( p, type(p) )