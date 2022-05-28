import math
import os
import random
import re
import sys
def findMedian(arr):
    x=sorted(arr)
    z=len(arr)//2
    y=len(arr)
    if y%2==0:
        return((x[(y-1)/2]+x[(y)/2])/2)
    else:
        return(x[z])
    # Write your code here

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().strip().split()))

    result = findMedian(arr)
    
    print(result)
