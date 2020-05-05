#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
 x=0
 y=0
 c=0
 d=0
 w=0
 z=0


 for i in range(0,5,+1):
   if (arr[x]>arr[c]):
      x=x
   elif (arr[x]<arr[c]):
      x=copy.copy(c)
   c=c+1

 for j in range(0,5,+1):
    if (arr[y]<arr[d]):
        y=y
    elif (arr[y]>arr[d]):
        y=copy.copy(d)
    d=d+1        

 w=sum(arr)-arr[y]
 z=sum(arr)-arr[x]


 print(z,w)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
