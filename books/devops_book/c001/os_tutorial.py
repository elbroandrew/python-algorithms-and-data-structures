# use os only if my script is not going to be crossplatform
# because for each platform there is specific mehods in 'os' module
# such as: Windows os.O_TEXT, GNU/Linux os.CLOEXEC
import os

print(os.stat("text"))
p = os.stat("text")
print(oct(p.st_mode)[-3:])  # 644
os.chmod('text', 0o777)  # using chmod
p = os.stat("text")
print(oct(p.st_mode)[-3:])  # 777

# os.path.expandvars && os.path.expanduser
print(os.path.expanduser("~/.ssh"))  # подставит  '/home/andrew/.ssh' вместо тильды или ~user
print(os.path.expanduser("~"))
print(os.environ)
print(os.path.expandvars("$HOME/.ssh"))  # короче берет из окружения переменную и подставляет ее путь в виде $HOME или ${HOME}

