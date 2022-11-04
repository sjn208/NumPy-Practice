# Jasmine Sajna
# Problem 4. Normalize a matrix so each row sums to 1
import numpy as np


def normalize(M):
    """this function will normalize each row of a matrix to 1
    :param M: matrix of values
    :return: normalized matrix
    """
    arr = np.array(M)  # make the given matrix an array in numpy
    rows = [1/(arr.sum(axis=1))]  # divide 1 by the sum of each row

    # the normalized values are the og values multiplied to be a fraction of the sum
    normalized = arr * np.transpose(rows)
    return normalized


g = [[3, 6, 9], [8, 6, 12], [2, 10, 6]]
print('original matrix: \n', g)
print('normalized matrix: \n', normalize(g))
