import sqlite3

# we need to validate and nuance the input

def customRead(w):
    '''read specific members fro mthe database'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # SQL = will find an exact match
    # SQL LIKE can make a case-insensitive match
    # SQL LIKE allows wildcards: %s ends-with s% begins-with %s% contains
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature LIKE "%{w}%"
    '''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close()
    except Exception as e:
        print(e)
    return rows

if __name__ == '__main__':
    w = input('Which creature? ')
    r = customRead(w)
    # iterate over any results
    for animal in r:
        print(f'We have {animal[1]} {animal[0]} costing {animal[2]}')