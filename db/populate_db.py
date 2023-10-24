import sqlite3

def populateDB(creatures_t):
    '''put all the creatures in the zoo'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # it is safest to use ? for insert, so we can validate
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures_t:
        try:
            if type(item['creature'])==str:
                n = item['creature']
            else:
                raise Exception('Creature name must be a string')
            if type( item['count'] )==int:
                count = item['count']
            else:
                raise Exception('Creature count must be an integer')
            if type(item['cost'])==float:
                cost = item['cost']
            else:
                raise Exception('Creature cost must be a float')
            # if all good, we can commit this value to the db
            curs.execute(st, (n, count, cost))
            conn.commit()
        except Exception as e:
            print(e)
    # after iterating over all the creatures, we can close the connection
    if conn:
        conn.close()

if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    populateDB(creatures_t)