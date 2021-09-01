#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    x=0 #currentposition
    y=0 #numberofjumps
    a=len(c)-1 #lastcloudposition
    b=len(c)-2 #lastsecondposition
    while x<b:
        x=x+1 if c[x+2] else x+2
        y+=1
    if x<a:
        y+=1
    return y
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
