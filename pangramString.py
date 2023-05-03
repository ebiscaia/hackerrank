# Eduardo Biscaia de Queiroz
# 03/05/2023

# A pangram is a string that contains every letter of the alphabet. Given a
# sentence determine whether it is a pangram in the English alphabet. Ignore
# case. Return either pangram or not pangram as appropriate.

# Example
# s= 'The quick brown fox jumps over the lazy dog'
# The string contains all letters in the English alphabet, so return pangram.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    sSplit = s.split()
    s = ""
    for sS in sSplit:
        s += sS

    s = s.lower()
    for i in range(97, 123):
        if chr(i) not in s:
            return "not pangram"

    return "pangram"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = "We promptly judged antique ivory buckles for the next prize"
    # s = "cavalo BOi"

    result = pangrams(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
