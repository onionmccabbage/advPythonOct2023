# we can write to files and read from files
# here is a file access object
# 'a' will append text (text is the default)
# 'x' is exclusive access - fails if the file already exists
# 'w' will (over)write
fout = open('snip.txt', 'a') 
# remember 'print' will always add a new line character at the end
print('here is a snippet of text', file=fout) #  end=', '
fout.close() # always a good idea to clean up

# often we need a more controlled way to write
def writeTextTofile(t):
    '''use a file access object to commit text to a text file'''
    try:
        # a file access object
        fout = open('my_log.txt', 'at') # 't' for text (the default)
        # fout.write(t) # could take a while to write a load of text
        size   = len(t)
        offset = 0
        chunk  = 12 # choose twelve characters at a time in this case
        while True:
            if offset > size:
                fout.write('\n') # terminate our output with sa new line character
                break # always provide a means to exit an endless loop!!
            else:
                # use slicing to write a part of the text
                part = t[offset:offset+chunk]
                fout.write(part) # write 12 character
                offset += chunk
        fout.close()
    # it is a good idea to handle specific exceptions
    except FileExistsError as fe:
        print(f'The file already exists {fe}')
    # ... then handle any generic exception
    except Exception as e:
        print(e)
    finally:
        pass # this always runs


if __name__ == '__main__':
    t = 'this might be a very large amount of text that we need to persist into a file without blocking the main thread'
    writeTextTofile(t)