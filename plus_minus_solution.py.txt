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
    # Write your code here
    pos = 0
    neg = 0
    res = 0
    for i in arr:
        if i == 0:
            res+=1
        elif i > 0:
            pos+=1
        else:
            neg+=1
            
    print("{0:.6f}".format(pos/n))
    print("{0:.6f}".format(neg/n))
    print("{0:.6f}".format(res/n))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
