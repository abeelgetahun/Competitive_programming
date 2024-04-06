#https://www.hackerrank.com/challenges/countingsort1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    if arr==None or len(arr)<=1:
        return
    count=[0]*(100)
    for i in arr:
        count[i]+=1
    print("".join(str(count).strip("[]").split(",")))
    

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    countingSort(arr)

    
