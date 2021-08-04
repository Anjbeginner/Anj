import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
  Cat_A=abs(x-z)
  Cat_B=abs(y-z)
  if (Cat_A<Cat_B):
    return('Cat A')
  elif(Cat_A>Cat_B):
    return('Cat B')
  elif(Cat_A==Cat_B):
    return('Mouse C')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
