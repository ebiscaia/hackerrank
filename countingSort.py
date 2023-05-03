# Eduardo Biscaia de Queiroz
# 02/05/2023

# Calculate the frequency of a number in an array

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    countElements=[]
    for i in range(0,100):
        countElements.append(arr.count(i))

    return countElements

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))

    arr = [10,1,0,4,5,4,20,8,4,10,11,20,13,14,10,4,5,8,4,20]
    result = countingSort(arr)
    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
