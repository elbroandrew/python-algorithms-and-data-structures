import socket

def get_socket_timeout():
    """
    function returns the socket timeout
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" % s.gettimeout())
    s.settimeout(100)
    print("Current timeout: %s" % s.gettimeout())

if __name__ == '__main__':
    get_socket_timeout()


"""
Default socket timeout: None
Current timeout: 100.0
"""