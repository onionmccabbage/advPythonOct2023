# we can build a socket client
import socket

def client():
    '''this is a basic socket client to interact with our socket server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    client.connect(port_t)
    # we can send a message to the server
    message = 'quit'
    # all http traffic must be url-encoded
    client.send(message.encode())
    # we can handle any response from the server
    data = client.recv(1024)
    print(f'Client received {data}')
    #remember to tidy up
    client.close()

if __name__ == '__main__':
    client()