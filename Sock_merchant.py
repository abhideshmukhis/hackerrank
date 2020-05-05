#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    y=[]

    x=set(ar)
    m=list(x)
    p=len(m)
    b=0


    for i in range(0,p,+1):
        
        y=ar.count(m[i])
        if y%2 ==0:
            y=y/2
        else: y=(y-1)/2

        b=b+y

    return(int(b))    






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
