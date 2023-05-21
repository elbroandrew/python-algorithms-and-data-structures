import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the size of the socket's send buffer
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [BEFORE]:%d" % bufsize)
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE
    )
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [AFTER]:%d" % bufsize)

if __name__ == '__main__':
    modify_buff_size()

'''
Buffer size [BEFORE]:65536
Buffer size [AFTER]:4096
'''