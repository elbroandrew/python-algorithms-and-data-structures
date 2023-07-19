import os


rc_name = ".examplerc"
var_name = "EXAMPLE_RC_DIR"
var_path = os.path.join(os.getcwd(), rc_name)
os.environ[var_name] = var_path
config_path = os.path.expandvars(var_path)  # не надо, наверно, т.к. нет глобальных переменных в пути?
print(config_path)
print(os.environ.items())

# print rc file current dir
rc_file_dir = os.path.abspath(__name__) # will get full path and __name__ at the end
parent_path = os.path.dirname(rc_file_dir)  # will get full path w/o __name__ (only current dir the file resides)
current_path = os.path.join(parent_path, rc_name)
print(current_path)

if var_name in os.environ:
    pass

