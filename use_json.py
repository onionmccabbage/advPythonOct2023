import json
from using_json import retrieve

# retrieve some JSON (from an API or from a file)
def getJSON():
    '''open a text file and read in all the text'''
    fin = open('review2/todos.json', 'rt')
    j = fin.read()
    fin.close()
    return j

if __name__ == '__main__':
    # convert the retrieved JSON into a structure
    s = retrieve(getJSON())
    # show the structure
    print(s)