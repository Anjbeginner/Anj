#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    w=list(w)
    x=len(w)-1
    while x>0 and w[x-1]>=w[x]:
        x-=1
    if x<=0:
        return('no answer')
    y=len(w)-1
    while w[y]<=w[x-1]:
        y-=1
    w[x-1],w[y]=w[y],w[x-1]
    w[x:]=w[len(w)-1:x-1:-1]
    return ''.join(w)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(raw_input().strip())

    for T_itr in xrange(T):
        w = raw_input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
