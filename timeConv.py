# Eduardo Biscaia de Queiroz
# 27/04/2023

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

import sys
import re
import random
import os
import math

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    timeArray12 = s.split(":")
    endArray = timeArray12[2]
    timeArray12[2] = endArray[0:2]
    timeArray12.append(endArray[2:])

    i = 0
    timeArray24 = ""
    while i < len(timeArray12) - 1:
        if i == 0 and timeArray12[-1] == "PM":
            timeArray12[i] = str(int(timeArray12[i]) + 12)

        if i == 0 and int(timeArray12[i]) % 12 == 0:
            timeArray12[i] = str(int(timeArray12[i]) - 12)

        if i == 0 and timeArray12[0] == "0":
            timeArray12[i] += "0"

        timeArray24 += timeArray12[i]
        timeArray24 += ":"
        i += 1
    return timeArray24[:-1]


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + "\n")

    # fptr.close()
