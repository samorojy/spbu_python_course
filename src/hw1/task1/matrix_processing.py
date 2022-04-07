from math import prod
from typing import List

Matrix = List[List[int]]


def check_matrix_format_correction(*matrices: Matrix):
    for matrix in matrices:
        columns_number = len(matrix[0])
        for row in matrix:
            if len(row) != columns_number:
                raise ValueError("Incorrect matrix format")


def get_matrices_multiplication_product(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    check_matrix_format_correction(matrix1, matrix2)
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Incorrect matrix format for multiplication")
    return [
        [sum([prod(elements) for elements in zip(row, column)]) for column in get_transposed_matrix(matrix2)]
        for row in matrix1
    ]


def get_transposed_matrix(matrix: Matrix) -> Matrix:
    check_matrix_format_correction(matrix)
    return [list(column) for column in zip(*matrix)]


def get_matrices_sum(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    check_matrix_format_correction(matrix1, matrix2)
    return [[sum(elements) for elements in zip(rows[0], rows[1])] for rows in zip(matrix1, matrix2)]


def print_matrix(matrix: Matrix):
    for row in matrix:
        print(row)
