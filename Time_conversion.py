#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
 if s[8]=="A":
      if s[:2]=="12":
            res="00"+s[2:-2]
      else: res=s[:-2]
 else:
      if s[:2]=="12":
            res=res=s[:-2]
      else: res=str(int(s[:2]) + 12)+s[2:-2]
    
 return (res)

  
#
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
