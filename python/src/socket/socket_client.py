import socket


def start_client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 12345))
    clientsocket.send('Hello, server!'.encode('utf-8'))
    msg = clientsocket.recv(1024)
    print(msg.decode('utf-8'))
    
    
if __name__ == '__main__':
    start_client()
