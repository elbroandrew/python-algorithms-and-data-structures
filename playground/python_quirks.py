# p = [1,2,3,4]

# # print(p[5:])


# #----------

# txt = "python"

# # txt[2].upper()
# # for i in range(len(txt)):
# #     txt[i] = txt[i].upper()
# # print(txt)

# #------------

# data = [10, '5', '', 0, None, True, False]

# result = list(filter(None, data))   # if None -> returns all items that are TRUE
# # print(result)   # [10, '5', True]

# #----------------
# d = {}
# d[1] = "a"
# d[True] = "b"
# # print(d)  # {1: 'b'}

# x = {1 : 'a', True: 'b'}
# # print(x[1])  # 'b'

# #----------
# s = {*()}  # --> получим SET

# # -------
# data_2 = [1,2,3]
# new_data = data_2 * 1
# # print(new_data)  # [1,2,3]
# # print(id(data_2))
# # print(id(new_data))

# #------
# def f(d:str):
#     return len(d)

# def f(num:int):
#     return(num**2)

# # print(f(10) + f("bee"))

# # ----------

squares = map(lambda n: n**2, [1,2,3])
print(type(squares))
sum(squares)
print(list(squares)) # [1, 4, 9] 
print(sum(squares), list(squares)) # 14 []

