import os

path = "../tests.py"

f = os.path.getsize(path)
print(f)


# better solution (more quicker)
def get_file_size(file_path: str):
    return os.stat(file_path).st_size


print(get_file_size("C:"))