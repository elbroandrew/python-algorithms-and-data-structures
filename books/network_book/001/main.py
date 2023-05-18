import socket

host_name = "www.python.org"

print(f"the IP of {host_name} is {socket.gethostbyname(host_name)}")
