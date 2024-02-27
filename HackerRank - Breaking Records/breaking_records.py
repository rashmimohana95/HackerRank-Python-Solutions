#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    min_ele = max_ele = scores[0]
    result = []
    mincount = 0
    maxcount = 0
    for i in range(len(scores)):
        if scores[i] > max_ele:
            max_ele = scores[i]
            maxcount+=1
        elif scores[i] < min_ele:
            min_ele = scores[i]
            mincount+=1
     
        
    result.append(maxcount)
    result.append(mincount)
    return result
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
