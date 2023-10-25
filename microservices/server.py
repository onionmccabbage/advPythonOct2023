# 'socket' provides all we need for socket programming (ie server/client)
import socket

def server():
    '''this microservice will listen for requests and respond
    It will be available over an http port (IP Internet Protocol)'''
    # we need some port settings
    port_t = ('localhost', 9874) # or a fixed IP address
    # now we create a server. Here are sensible defaults
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(port_t)
    # we can begin listening for requests
    server.listen() # we can set a listening backlog...
    print(f'Server is listening on port {port_t[1]} address {port_t[0]}')
    # we need a 'run loop'
    while True: # endless loop
        # unpack any request received
        (client, addr) = server.accept() 
        print(f'Request received from {client}, {addr}')
        # read a portion of the client stream
        buf = client.recv(1024) # just the first 1024 bytes
        print(f'server received {buf}')
        # we can choose to send a response
        client.send( buf.upper() )
        client.close()

if __name__ == '__main__':
    # start our server
    server()