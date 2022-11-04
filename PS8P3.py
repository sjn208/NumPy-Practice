# Jasmine Sajna
# problem 3. function returns local maxima of array
import numpy as np


def local_maxes(arr):
    """function to get the local maxes of a 1d array
    :param arr: 1d array of integers
    :return: array of integers (max values)
    """
    centerArr = arr[1:-1]  # array of the center values to exclude edges
    left = arr[:-2]  # shifts OG values to get left side values at each center
    right = arr[2:]  # shifts OG values to get right side values at each center
    maxes = centerArr[(centerArr > left) & (centerArr > right)]  # copy center values who're larger than their neighbors
    return maxes


vec = np.array([3, 6, 8, 2, 7, 3])
print(f'maxes of {vec} are: {local_maxes(vec)}')
