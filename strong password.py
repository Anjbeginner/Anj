import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    result=0
    if not any(i in  numbers for i in password ):
        result+=1
    if not any(i in  lower_case for i in password ):
        result+=1
    if not any(i in  upper_case for i in password ):
        result+=1
    if not any(i in  special_characters for i in password ):
        result+=1
    if (len(password)<6):
        return max(result,6-len(password))
    return result
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
