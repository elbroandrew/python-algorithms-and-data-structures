p = [1,2,3,4]

# print(p[5:])


#----------

txt = "python"

# txt[2].upper()
# for i in range(len(txt)):
#     txt[i] = txt[i].upper()
# print(txt)

#------------

data = [10, '5', '', 0, None, True, False]

result = list(filter(None, data))   # if None -> returns all items that are TRUE
# print(result)   # [10, '5', True]

#----------------
d = {}
d[1] = "a"
d[True] = "b"
# print(d)  # {1: 'b'}

x = {1 : 'a', True: 'b'}
# print(x[1])  # 'b'

#----------
s = {*()}  # --> получим SET