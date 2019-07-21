#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
def sorting(l):
    swaps = 0
    for x in range(len(l)-1,0,-1):
        for i in range(x):
            if(l[i]>l[i+1]):
                l[i],l[i+1]=l[i+1],l[i]
                swaps +=1
    return swaps

print("Array is sorted in "+str(sorting(a)) + " swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])



