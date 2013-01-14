__author__ = 'hugohenley'

import numpy as np

file_1 = open('matrix_1.txt', 'r')
matrix_1 = file_1.read()

file_2 = open('matrix_2.txt', 'r')
matrix_2 = file_2.read()

matrix_1_m = matrix_1.replace('\n', '; ')
matrix_np = np.matrix(matrix_1_m)
matrix_2_m = matrix_2.replace('\n', '; ')
matrix_np2 = np.matrix(matrix_2_m)

print matrix_np * matrix_np2