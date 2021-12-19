nested_list = [[1,2,3], [4,5,6], [7,8,9]]
[[print(val) for val in element] for element in nested_list]


# tic tac toe
board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)

