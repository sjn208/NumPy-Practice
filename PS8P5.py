# Jasmine Sajna
# Problem 5. Count the occurrences of each value 0-9 in a 5x5 random matrix
import numpy as np


def occurrences(mat):
    """this function finds the diff values and occurrences of each value in a 2d matrix
    :param mat: 2d (5x5) matrix
    :return: no return, (prints values)
    """
    arr = np.array(mat)  # make 5x5 a numpy array
    values, counts = np.unique(arr, return_counts=True)  # store the unique values & occurrences

    # to display the values and their respective occurrences together, use zip
    for value, count in zip(values, counts):
        print(f'Value {value} occurs {count} times.')


# make a 5x5 matrix of random values 0-9 and display
matr = np.random.randint(0, 10, 25).reshape(5, 5)
print('Random 0-9 values 5x5 matrix: ')
print(matr, '\n')

occurrences(matr)  # call fn
