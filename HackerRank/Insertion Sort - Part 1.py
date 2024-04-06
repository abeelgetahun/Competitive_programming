#https://www.hackerrank.com/challenges/insertionsort1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    k=len(arr)-1
    while arr[k-1]>arr[k] and k>0:
        temp=arr.copy()
        temp[k-1],temp[k]=temp[k-1],temp[k-1]
        arr[k-1],arr[k]=arr[k],arr[k-1]
        temp=str(temp)
        print("".join(temp.strip("[]").split(",")))
        k-=1
    final=str(arr)
    print("".join(final.strip("[]").split(",")))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().strip().split()))

    insertionSort1(n, arr)
