from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
	maxi = arr[0]
	sumi = 0
	for i in range(0,n):
		sumi += arr[i]
		
		if sumi < 0:
			sumi = 0
		if sumi > maxi :
			maxi = sumi

		
		
	maxi = max(sumi,maxi)
	return maxi

#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
