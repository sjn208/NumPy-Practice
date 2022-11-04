# Jasmine Sajna
# problem 2: return the closest value in an array to a value
import numpy as np


def get_closest(arr, v):
    """function to find the closest value of an array to a value v
    :param arr: vector
    :param v: integer
    :return: vector of one value at index
    """
    A = np.array(arr)  # make given vector a numpy array
    diffA = abs(A-v)  # store the absolute value diff of the vectors and v in an array
    index = np.argmin(diffA)  # get index of min diff
    return A[index]  # use min diff index for index in original

array = [10, 3, 7, 8, 15]
print(f'closest value in {array} to 4 is {get_closest(array, 4)}')
      
