#!/bin/python3

import math
import os
import random
import re
import sys

#creating a loop for performing tables

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(0,10):
        x=(i+1)*n
        i+=1
        print('%d x %d = %d' %(n,i,x))
