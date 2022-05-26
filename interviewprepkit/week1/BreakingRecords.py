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
  hi=scores[0]
  lo=scores[0]
  mini=0
  maxi=0
  for i in range(len(scores)):
    if scores[i]<lo:
      lo=scores[i]
      mini+=1
    if scores[i]>hi:
      hi=scores[i]
      maxi+=1
  return [maxi,mini]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
