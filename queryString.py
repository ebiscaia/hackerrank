# Eduardo Biscaia de Queiroz
# 28/04/2023

# There is a collection of input strings and a collection of query strings. For
# each query string, determine how many times it occurs in the list of input
# strings. Return an array of the results.
# Example:
# strings = ["ab", "ab", "abc"]
# query = ['ab', 'abc', 'bc']
# There are  instances of ',  of '' and  of ''. For each query, add an element
# to the return array,
# results = [2, 1, 0]

#!/bin/python3

import math
import os
import random
import re
import sys


def matchingStrings(strings, queries):
    results = []
    for query in queries:
        results.append(strings.count(query))
    return results


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # strings_count = int(input().strip())
    #
    # strings = []
    #
    # for _ in range(strings_count):
    #     strings_item = input()
    #     strings.append(strings_item)
    #
    # queries_count = int(input().strip())
    #
    # queries = []
    #
    # for _ in range(queries_count):
    #     queries_item = input()
    #     queries.append(queries_item)
    #
    strings = ["aba", "baba", "aba", "xzxb"]
    query = ["aba", "xzxb", "ab"]
    res = matchingStrings(strings, query)
    print(res)
    #
    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
