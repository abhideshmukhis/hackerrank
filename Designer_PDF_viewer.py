#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    list1=list(word)
    s=0
    for i in range(0,len(list1)):
        m=ord(list1[i])-97
        if h[m]>s:
            s=h[m]
        

    p=s*len(list1)
    return(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
