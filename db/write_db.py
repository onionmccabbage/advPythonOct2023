import sqlite3

def writeDB():
    '''populate our database with animals'''
    conn = sqlite3.connect('my_db') #connect to the db
    curs = conn.cursor()
    # sql statement
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.52)
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    writeDB()