#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maxi=arr[0]
    mini=arr[0]
    ans=0
    ans1=0
    ans2=0
    for i in range(len(arr)):
        maxi=max(arr)
        mini=min(arr)
    for i in arr:
        ans = ans+i
    ans1 = ans - maxi
    ans2 = ans - mini
    print(ans1,ans2)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
