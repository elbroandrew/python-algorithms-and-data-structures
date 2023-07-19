import sys, os

print(sys.byteorder)  # little endian
print(sys.platform)
print(sys.getsizeof(1))
print(sys.version_info.major)
print(sys.version_info.minor)

os.chmod("using_subprocess.py", 777)
