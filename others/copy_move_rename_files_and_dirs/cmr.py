import os, shutil

print(os.listdir())

# copy
shutil.copy("testfile1", "backup.txt")

print(os.stat("testfile1"),
      os.stat("backup.txt"), sep="\n")  # st_time different

shutil.copytree("dir2", "new_folder_1")  # copy all files from dir2 into new_folder_1

shutil.move("testfile1", "dir1/test1.txt")
os.rename("dir1/test1", "backup.txt")
