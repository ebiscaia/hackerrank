# Name: Eduardo Biscaia de Queiroz
# Date: 30/04/2023

# You will be given a list of 32 bit unsigned integers. Flip all the bits 1->0 and 1->0 and return the result as an unsigned integer.

# Example
# n = 9 (base 10)
# 9(10) = 1001(2). We're working with 32 bits, so:
# 00000000000000000000000000001001(2) = 9(10)
# 11111111111111111111111111110110(2) = 4294967286(10)
# Return 4924967286

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.


def maxPower(n):
    i = 0
    while pow(2, i) <= n:
        i += 1
    if n == 0:
        i = 1
    return i


def binary(n, lenN):
    bin = ""
    if n == 0:
        return "0"
    while lenN >= 0:
        if n >= pow(2, lenN):
            bin += "1"
            n -= pow(2, lenN)
        else:
            bin += "0"
        lenN -= 1
    return bin


def bin32(bin):
    return "0" * (32 - len(bin)) + bin


def flipDigits(bin32Number):
    flippedNumber = ""
    for _ in bin32Number:
        if _ == "0":
            flippedNumber += "1"
        else:
            flippedNumber += "0"
    return flippedNumber


def flippingBits(n):
    lenN = maxPower(n)
    bin = binary(n, lenN)
    bin32Numb = bin32(bin)
    flippedNumber = flipDigits(bin32Numb)
    flippedNumberDecimal = 0
    index = -1
    while index > -33:
        if flippedNumber[index] == "1":
            flippedNumberDecimal += pow(2, -index - 1)
        index -= 1
    return flippedNumberDecimal


if __name__ == "__main__":
    #    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #     q = int(input().strip())

    #    for q_itr in range(q):
    #        n = int(input().strip())
    n = [4294967295, 16, 1, 0]
    for nb in n:
        result = flippingBits(nb)
        print(result)

#        fptr.wr
