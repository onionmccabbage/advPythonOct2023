import json # this is a library available to python

def main(s):
    '''take a python data structure and make it into a JSON structure'''
    j = json.dumps(s) # convert any python structure into JSON
    return j

def retrieve(j):
    '''convert JSON into a pythno structure'''
    s = json.loads(j) # make the JSON into a python structure (list, dict etc)
    return s

# we only want to run the following if this is the main module
if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )  
    result_j = main(creatures_t)
    print(result_j, type(result_j))
    results_s = retrieve(result_j)
    print(results_s, type(results_s))
