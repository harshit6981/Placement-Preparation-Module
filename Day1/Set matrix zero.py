from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    rows, columns = len(matrix), len(matrix[0])

    # Use the first row and first column as markers
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(columns))
    first_column_has_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Find the cells to be set to 0 and mark the first row and first column
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set the marked cells to 0
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set the first row and first column to 0 if necessary
    if first_row_has_zero:
        for j in range(columns):
            matrix[0][j] = 0

    if first_column_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix
