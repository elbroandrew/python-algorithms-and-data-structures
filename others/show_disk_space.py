from psutil import disk_usage


total, used, free, percent = disk_usage('C:')
print(total / 1024 / 1024 / 1024)
print(used / 1024 / 1024 / 1024)
print(free / 1024 / 1024 / 1024)
