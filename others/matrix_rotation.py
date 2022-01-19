"""
Given a matrix, rotate it counter-clockwise 90 degrees.
[1, 2, 3,
 4, 5, 6,
 7, 8, 9]
becomes
[3, 6, 9,
 2, 5, 8,
 1, 4, 7]

"""
import math
from typing import List


def rotate_matrix(matrix: List) -> List:
    if len(matrix) <= 1:
        return matrix
    else:
        # 0 FIND NUMBERS OF ROWS
        rows_num = int(math.sqrt(len(matrix)))

        # 1 CREATE ROWS LISTS (SLICE BASE MATRIX INTO 2D LIST)
        list_2d = [matrix[x: x + rows_num] for x in range(0, len(matrix), rows_num)]

        # 2 ROTATE MATRIX
        rotated = [[] for x in range(0, rows_num)]

        for x1 in range(0, len(list_2d)):
            for x2 in range(0, rows_num):
                rotated[len(list_2d) - x1 - 1].append(list_2d[x2][x1])

        # 3 FLATTEN LISTS
        print([item for sublist in rotated for item in sublist])
        return [item for sublist in rotated for item in sublist]




def main():

    example_matrix = [1, 2, 3,
                      4, 5, 6,
                      7, 8, 9]

    rotate_matrix(example_matrix)


if __name__ == '__main__':
    main()
