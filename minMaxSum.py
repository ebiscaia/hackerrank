# Eduardo Biscaia de Queiroz
# 26/04/2023
# Second HackerRank Challenge

# Given five positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers. Then print the
# respective minimum and maximum values as a single line of two space-separated
# long integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min = 0
    max = 0
    i = 0
    while i < len(arr):
        if i == 0:
            min += arr[i]
        elif i == len(arr) - 1:
            max += arr[i]
        else:
            max += arr[i]
            min += arr[i]
        i += 1
    return f"{min} {max}"


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    print(miniMaxSum(arr))
