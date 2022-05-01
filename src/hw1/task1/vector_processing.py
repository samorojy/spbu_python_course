from math import sqrt, acos
from typing import List

Vector = List[int]


def check_vectors_correction(*vectors: Vector):
    for vector in vectors:
        if len(vector) != len(vectors[0]):
            raise ValueError("all vectors must be the same size!")


def get_vectors_scalar(vector1: Vector, vector2: Vector) -> int:
    check_vectors_correction(vector1, vector2)
    return sum(coordinate[0] * coordinate[1] for coordinate in zip(vector1, vector2))


def get_vector_length(vector: Vector) -> float:
    return sqrt(sum(coordinate**2 for coordinate in vector))


def get_vectors_angle(vector1: Vector, vector2: Vector) -> float:
    return acos(get_vectors_scalar(vector1, vector2) / (get_vector_length(vector1) * get_vector_length(vector2)))
