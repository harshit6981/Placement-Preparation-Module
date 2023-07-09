from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    hasharr = [0] * (n+1)
    n = len(arr)
    for i in range(n):
        hasharr[arr[i]] += 1

    repeating = -1
    missing = -1
    for i in range(1,n+1):
        if hasharr[i] == 2:
            repeating  = i
        elif hasharr[i] == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
    return (missing,repeating)



