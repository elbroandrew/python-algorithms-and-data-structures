#!/usr/bin/python3.9

import subprocess, os

"""
first make this file executable via chmod
after that run without 'python3 using_subprocess.py' just './using_subprocess.py'
"""

cp = subprocess.run(
    ['ls', '-l'],
    capture_output=True,  # capture stdout or stderr then write 'cp.stderr'
    universal_newlines=True,
)

print(cp.stdout)
