from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Find the largest index i such that permutation[i] < permutation[i+1]
    i = n - 2
    while i >= 0 and permutation[i] >= permutation[i+1]:
        i -= 1
    
    
    # If no such index exists, the given permutation is the last permutation
    if i < 0:
        return permutation[::-1]
    
    # Find the largest index j such that permutation[j] > permutation[i]
    j = n - 1
    while j > i and permutation[j] <= permutation[i]:
        j -= 1
    
    # Swap the elements at indices i and j
    permutation[i], permutation[j] = permutation[j], permutation[i]
    
    # Reverse the order of elements after index i
    left = i + 1
    right = n - 1
    while left < right:
        permutation[left], permutation[right] = permutation[right], permutation[left]
        left += 1
        right -= 1
    
    return permutation
