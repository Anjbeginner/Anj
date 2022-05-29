#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for i in range(0,len(grades)):
        if grades[i]<38:
            continue
        else:
            x=grades[i]
            re=x % 5
            if re==3:
                x+=2
                grades[i]=x
            elif re==4:
                x+=1
                grades[i]=x
            else:
                continue

    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
