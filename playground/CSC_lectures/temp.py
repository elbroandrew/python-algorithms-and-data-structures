import os, tempfile

# NamedTemporaryFile -- гарантирует, что у него будет какое-то имя в системе

with tempfile.NamedTemporaryFile() as file:  
    path = file.name
    print(path)