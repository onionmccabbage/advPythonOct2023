import sqlite3

def customUpdate(w):
    '''update the database'''
    q = int(float(w['count'])) # make sure it can be an int
    a = w['creature']
    # we could also deal with the cost...
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = f'''
    UPDATE zoo
    SET count={q}
    WHERE creature = "{a}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # we need to know which creature to update
    creature = input('Which creature? ')
    # new quantity
    q = input ('How many? ')
    # new cost
    c = input('Cost? ')
    # we can build a structure containing our values
    obj = {'creature':creature, 'count':q, 'cost':c}
    customUpdate(obj)
