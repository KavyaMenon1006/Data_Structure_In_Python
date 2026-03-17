#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    max_stack = []
    result = []
    for op in operations:
        num = op.split()  
        if num[0] == "1":  #push
            x = int(num[1])
            stack.append(x)
            if not max_stack or x >= max_stack[-1]:
                max_stack.append(x)
            else:
                max_stack.append(max_stack[-1])
        elif num[0] == "2":  #pop
            if stack:
                stack.pop()
                max_stack.pop()
        elif num[0] == "3":  #print max
            if max_stack:
                result.append(max_stack[-1])
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
