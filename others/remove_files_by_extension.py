import os


mypath = "C:\\Users\\user\\super secret folder"


def extract_ext(file_path):
    split_tuple = os.path.splitext(file_path)

    return split_tuple[0], split_tuple[1]

def abs_path(my_file_path, file_name):
    return f"{my_file_path}\\{file_name}"

subfolders_list = os.listdir(mypath)

subfolders_paths = [os.path.join(mypath, path) for path in subfolders_list]

    
for folder_path in subfolders_paths:
    files_list = os.listdir(folder_path)
    
    if len(files_list) != 0:   
            
        for file_name in files_list:
            file_abs_path = abs_path(folder_path, file_name)
            _, file_extension = extract_ext(file_abs_path)
            
            
            if file_extension == ".html" or file_extension == ".srt":
                os.remove(file_abs_path)
    else:
        os.rmdir(folder_path)
