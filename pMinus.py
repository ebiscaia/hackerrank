#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Start the variables. They count how many positive, negative and zero
    # elements that are included in the array
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos / len(arr):.6f}")
    print(f"{neg/ len(arr):.6f}")
    print(f"{zero/ len(arr):.6f}")


if __name__ == "__main__":
    # Enter the size of the array
    # A bit unnecessary as the function is defined to use only
    # the array
    n = int(input("Enter the size of the array: ").strip())
    # Enter the array elements separated by spaces
    arr = list(
        map(int, input("Type the numbers of the array using spaces: ").rstrip().split())
    )
    # Starts the function of the test
    plusMinus(arr)
