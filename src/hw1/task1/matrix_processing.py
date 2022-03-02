from math import prod
from typing import List


def check_matrix_format_correction(*matrices: List[List[int]]):
    for matrix in matrices:
        columns_number = len(matrix[0])
        for row in matrix:
            if len(row) != columns_number:
                raise ValueError("Incorrect matrix format")


def get_matrices_multiplication_product(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    check_matrix_format_correction(matrix1, matrix2)
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Incorrect matrix format for multiplication")
    return [
        [sum([prod(elements) for elements in zip(row, column)]) for column in get_transposed_matrix(matrix2)]
        for row in matrix1
    ]


def get_transposed_matrix(matrix: List[List[int]]) -> List[List[int]]:
    check_matrix_format_correction(matrix)
    return [list(column) for column in zip(*matrix)]


def get_matrices_sum(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    check_matrix_format_correction(matrix1, matrix2)
    return [[sum(elements) for elements in zip(rows[0], rows[1])] for rows in zip(matrix1, matrix2)]


def print_matrix(matrix: List[List[int]]):
    for row in matrix:
        print(row)
