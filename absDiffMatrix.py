# Eduardo Biscaia de Queiroz
# 01/05/2023

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown bellow:
#
# 1   2   3
# 4   5   6
# 9   8   9
#
# The left to right diagonal = 1+5+9   = 15.
# The right to left diagonal = 9+5+3   = 17.
# The absolute difference    = |15-17| = 2.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    sumLRight = 0
    sumRLeft = 0
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr):
            if i == j:
                sumLRight += arr[i][j]
            if i + j == len(arr) - 1:
                sumRLeft += arr[i][j]
            j += 1
        i += 1
    return abs(sumLRight - sumRLeft)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    #
    # n = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[6, 8], [-6, 9]]
    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + "\n")
    #
    # fptr.close()
