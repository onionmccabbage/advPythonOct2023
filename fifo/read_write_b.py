# we can write and read bytes
def makeBytes(values):
    '''make a byte string fro mthe values'''
    b = bytes(values) # convert the string into bytes
    return b

def writeBytes(b):
    '''commit the bytes to a byte file'''
    try:
        # remember  this is a file access object
        fout = open('bfile', 'wb') # 'w' will (over)write 'b' for bytes
        fout.write(b)
        fout.close()
    except Exception as e:
        print(e)

def readBytes():
    '''retrieve bytes from a byte file'''
    fin = open('bfile', 'rb')
    retrieved_b = fin.read()
    return retrieved_b

if __name__ == '__main__':
    v = range(0,256)
    b = makeBytes(v)
    # commit these bytes to our byte file
    writeBytes(b)
    z = readBytes()
    print(z) # b'...' indicates a byte string
