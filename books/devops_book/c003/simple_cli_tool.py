#!/usr/bin/python3.9

import sys

if __name__ == '__main__':
    print(sys.argv[0])  # here is the name of my script  as value 0
    print(sys.argv[1])  # value 1
    print(sys.argv[2])  # value 2
    print(sys.argv[3])  # value 3

# then run and pass some args: ./simple_cli_tool.py --a-flag value 100


