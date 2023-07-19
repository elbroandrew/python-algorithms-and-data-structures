import subprocess, os


cp = subprocess.run(
    ['ls', '-l'],
    capture_output=True,  # capture stdout or stderr then write 'cp.stderr'
    universal_newlines=True,
)

print(cp.stdout)
