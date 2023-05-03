# Eduardo Biscaia de Queiroz

# Given an array of integers, where all elements but one occur twice, find the unique element.
# Example
# a = [1, 2, 3, 4, 3, 2, 1]
# The unique element is 4.


#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    elements = []
    countElements = []
    for _ in a:
        if _ not in elements:
            elements.append(_)
            countElements.append(a.count(_))

    for index, count in enumerate(countElements):
        if count == 1:
            return elements[index]


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    #
    # n = int(input().strip())
    #
    # a = list(map(int, input().rstrip().split()))

    a = [1, 2, 3, 4, 3, 2, 1]
    result = lonelyinteger(a)
    print(result)

    # fptr.write(str(result) + "\n")
    # fptr.close()
