# Jasmine Sajna
# Problem 1. Create an array with shape n, m of all zeros except border
import numpy as np


def zero_ones(n, m):
    """ function to create matrix of size n,m with border of 1s and inner 0s
    :param n: row size
    :param m: col size
    :return: matrix
    """
    mat = np.zeros((n, m)) # make matrix of all 0s

    mat[0, :] = 1  # changes top to 1s
    mat[-1, :] = 1  # changes bottom to 1s
    mat[:, 0] = 1  # changes sides to 1s
    mat[:, -1] = 1

    return mat


# take row and column size from user
n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))
print(zero_ones(n, m))


