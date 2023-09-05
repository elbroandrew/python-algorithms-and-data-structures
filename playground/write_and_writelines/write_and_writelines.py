

# with open("playground/write_and_writelines/data.txt", 'r+') as file:
#     print("some text 1", file=file)


f = open("playground/write_and_writelines/data.txt", 'w')

print("some text2", file=f)


f.close()
