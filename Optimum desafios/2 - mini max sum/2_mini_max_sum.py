#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ## ordena o vetor recebido  
    arr.sort()

    ## calcula soma minima, somado de arr[0] ate arr[3]
    s_min = sum(arr[0:4])
    ## calcula soma maxima, somando de arr[1] ate arr[4]
    s_max = sum(arr[1:5])

    print(s_min, s_max)

    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)