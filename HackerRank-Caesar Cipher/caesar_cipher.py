#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = ''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = k% 26
    for i in range(n):
        if s[i] in lower:
            result+= (chr((ord(s[i])+k))) if ((ord(s[i])+k) <=ord('z')) else (chr(ord('a')-1 + (ord(s[i])+k)- ord('z')))
             
        elif s[i] in upper:
            result+= (chr((ord(s[i])+k))) if ((ord(s[i])+k) <=ord('Z')) else (chr(ord('A')-1 + (ord(s[i])+k)- ord('Z')))
            
        else:
            result+= s[i]
    
    return result
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
