import sqlite3 # this database comes with python

def accessDB():
    '''create a database then make a table for zoo animals'''
    conn = sqlite3.connect('my_db') # either create the database or connect to it if it exists
    curs = conn.cursor() # this is a database access mechanism
    # we need an SQL statement
    st = '''
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost, float
    )
    '''
    try:
        curs.execute(st) # use thet cursor to send the SQL statemetn ot the database
        conn.commit() # make sure the statement is committed
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    accessDB()