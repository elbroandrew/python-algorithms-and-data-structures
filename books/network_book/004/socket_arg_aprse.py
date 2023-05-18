import sys, socket, argparse

"""
This script shows how to handle socket errors.
"""



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

    # Create a socket -- First try-except block
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print()