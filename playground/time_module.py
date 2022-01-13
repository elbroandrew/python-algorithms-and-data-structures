import time

# print(time.ctime(0)) # converts a time expressed in sconds since epoch to a readable string

# print(time.time()) # returns current time since epoch in seconds

# print(time.ctime(time.time()))

# time_obj = time.localtime() # get object of date
# print(time_obj)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_obj) # convert it to readable string, for 'format' see docs.
# print(local_time)
# if you need UTC:
# time_obj = time.gmtime()

# from a string
# time_string = "20 April, 1999"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# tuple with (year, month, day, hours, minutes, seconds, day_of_week, day_of_year, day_saving_time)
time_tuple = (1999, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)
print(time.mktime(time_tuple)) # convert into timestamps
