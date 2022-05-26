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
    x=0
    y=0
    z=0
    for i in range(len(arr)):
        if arr[i]>0:
            x+=1
        elif arr[i]<0:
            y+=1
        else:
            z+=1
    print(x/(len(arr)))
    print(y/(len(arr)))
    print(z/(len(arr)))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
