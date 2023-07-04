import socket

'''simple internet TCP socket'''
'''there is also Unix socket for interprocess communication on one machine'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # stream means TCP connection
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen()
print('server is listening for TCP connection')

client_socket, client_addr = server_socket.accept()
print('Connection from: ', str(client_addr))

for _ in range(10):
    msg = client_socket.recv(1024).decode()
    print('data from client: ', str(msg))

client_socket.close()
