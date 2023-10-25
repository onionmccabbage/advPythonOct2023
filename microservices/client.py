# we can build a socket client
import socket
# we can read system argument variables
import sys

def client():
    '''this is a basic socket client to interact with our socket server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    client.connect(port_t)
    # we can send a message to the server
    # check if there were aditional system argument variables
    if len(sys.argv) > 1: # there will always be at least one sys.argv (the module name)
        message = ' '.join(sys.argv[1:]) # ignore member zero
    else:
        message = 'default' # we can send 'quit' as a system argument variable
    # all http traffic must be url-encoded
    client.send(message.encode())
    # we can handle any response from the server
    data = client.recv(1024)
    print(f'Client received {data}')
    #remember to tidy up
    client.close()

if __name__ == '__main__':
    client()