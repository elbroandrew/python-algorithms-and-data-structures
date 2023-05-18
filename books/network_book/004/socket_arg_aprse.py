import os, sys, socket, argparse, logging
from constants import LOG_DIR

"""
This script shows how to handle socket errors.
"""

# logging
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

#FIXME: LOG_DIR path may not be correct.
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

    # Create a socket -- First try-except block
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        logger.error("Error creating socket: %s" % e, exc_info=True) # exc_info=True means exception text will also be added into the log file.