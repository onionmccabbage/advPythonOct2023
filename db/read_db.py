import sqlite3

def readDB():
    '''access the database then retrieve all the values from the zoo table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
    SELECT creature, count, cost FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit()
        # we ca nnow read back any retreived data
        rows = curs.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(e)

if __name__ == '__main__':
    r = readDB() # gather all the rows from the database
    for animal in r:
        print(f'We have {animal[1]} {animal[0]} each costing {animal[2]}')