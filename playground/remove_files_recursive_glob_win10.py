import glob
import os
import fnmatch


# remove unnecessary files

path = r"\\?\C:\Users\user\Downloads\IBM Data Engineering Professional Certificate 2023-8\**"
# \\?\ -> в Вин10 ограничение снимает на длину пути в 260 символов.

for file_name in glob.glob(pathname=path, recursive=True):
    if os.path.isdir(file_name):
        continue
    
    if not fnmatch.fnmatch(file_name, '*.mp4'):
        try:

            os.remove(file_name)
            
            print(f"{file_name} was deleted.") 
            
        except Exception as e:
            print(e)