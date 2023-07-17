import os, shutil, zipfile

print(os.listdir())

with zipfile.ZipFile('first.zip', 'w') as z:
    z.write("file1.py")

with zipfile.ZipFile("first.zip", 'r') as z:
    print(z.filelist)  # [<ZipInfo filename='file1.py' filemode='-rw-rw-rw-' file_size=2>]

with zipfile.ZipFile("first.zip", 'r') as z:
    z.extract("file1.py", 'extracted/file1')

with zipfile.ZipFile('first.zip', 'w') as z:
    for f in os.listdir():
        z.write(f)

with zipfile.ZipFile('first.zip', 'r') as z:
    z.extractall('extracted_all/')

shutil.make_archive("made_with_shutil", 'zip')
shutil.unpack_archive("made_with_shutil.zip", extract_dir="from_shutil_archive")
