#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(p):
  s=p
  for i in range(p,0,-1):
    print(' ' * (p-1)+ '#' * (s-(p-1)))
    p=p-1


if __name__ == '__main__':
    n = int(input())

    staircase(n)
