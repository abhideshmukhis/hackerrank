#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    x=50
    flag=[]
    b=0
    

    for i in range(0,n,+1):
        if(s[i]=='D'):
            x=x-1
        else:
            x=x+1
        if(x<50):
            flag.append(1)
        else:
            flag.append(0)
            
    if flag[0]==1:
            b=b+1
    for i in range(0,(n-1),+1):
        if flag[i]==0:
            if flag[i+1]==1:
                 b=b+1
            
        
    return(b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
