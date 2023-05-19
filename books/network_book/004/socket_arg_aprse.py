import os, sys, socket, argparse, logging
from constants import LOG_DIR

"""
This script shows how to handle socket errors.
"""

# logging
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

fh = logging.FileHandler(f"{LOG_DIR}/all.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


def main():
    """
    setup argument parsing
    """
    parser = argparse.ArgumentParser(description="Socket Error Examples")
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # Create a socket -- first try-except block
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        logger.error("Error creating socket: %s" % e, exc_info=True)
        sys.exit(1)
    # Connect to given host/port -- second try/except block
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logger.error("Address-related error connecting to server: %s" % e, exc_info=True)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        logger.error("Connection error: %s" % e, exc_info=True)
        sys.exit(1)
    # Sending data -- third try/except block
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        logger.error("Error sending data: %s" % e, exc_info=True)
        sys.exit(1)
    while 1:
        # waiting to receive data from host -- fourth block
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            logger.error("Error receiving data: %s" % e, exc_info=True)
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == '__main__':
    main()



