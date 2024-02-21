#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    d = {'12': '00', '01': '13', '02': '14', '03': '15', '04': '16', '05': '17', '06': '18', '07': '19', '08': '20', '09': '21', '10': '22', '11': '23'}
    st = s.split(':')
    if 'PM' in s and st[0] == '12':
        result = s[0:8]
    if 'AM' in s:
        result = s[0:8]
    if 'AM' in s and st[0] == '12':
        if st[0] in d:
            first = d[st[0]]
            newstr = first+":"+st[1]+":"+st[2]
            result = newstr[0:8]
    if 'PM' in s and st[0] != '12':
        if st[0] in d:
            first = d[st[0]]
            newstr = first+":"+st[1]+":"+st[2]
            result = newstr[0:8]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
