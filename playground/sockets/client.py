import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('0.0.0.0', 8080))

msg = "Hello TCP socket"

for _ in range(10):
    client_socket.send(msg.encode())
    # or
    #client_socket.send(b'Hello')

client_socket.close()

