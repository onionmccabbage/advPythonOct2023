# 'socket' provides all we need for socket programming (ie server/client)
import socket
import sys

def writeToFile(data, fileName):
    '''we can log the server activity to a file'''
    # we really should use try-except
    fout = open(fileName, 'a')
    fout.write(f'{data}\n') # make sure every commit has a new line at the end
    fout.close()

# within this server we will send output to our log file
# this could be done using redirection
def server():
    '''this microservice will listen for requests and respond
    It will be available over an http port (IP Internet Protocol)'''
    # see if any sys.argv are provided (for the log file name)
    fileName = 'serverlog.txt'
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    # we need some port settings
    port_t = ('localhost', 9874) # or a fixed IP address
    # now we create a server. Here are sensible defaults
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(port_t)
    # we can begin listening for requests
    server.listen() # we can set a listening backlog...
    writeToFile(f'Server is listening on port {port_t[1]} address {port_t[0]}', fileName)
    # we need a 'run loop'
    while True: # endless loop
        # unpack any request received
        (client, addr) = server.accept() 
        # print(f'Request received from {client}, {addr}')
        writeToFile(f'Request received from {addr}', fileName)
        # read a portion of the client stream
        buf = client.recv(1024) # just the first 1024 bytes
        writeToFile(f'server received {buf}', fileName)
        # we can provide a mechanism to stop the server
        if buf==b'quit':
            writeToFile('Server is closing', fileName)
            server.close()
            break # stop the run-loop

        # we can choose to send a response
        client.send( buf.upper() )
        client.close()

if __name__ == '__main__':
    # start our server
    server()