'''
this code is solution of Company logo problem on hackerrank.

https://www.hackerrank.com/challenges/most-commons/problem
'''


#!/bin/python3

import math
import os
import random
import re
import sys
import operator
from collections import OrderedDict



if __name__ == '__main__':
    s = sorted(input())
    d = {}
    l = list(s)
    for i in l:
        if i not in (d):
            d[i] = 1
        else:
            d[i] += 1
occuracnce_list = []
d1= OrderedDict()
for key in sorted(d):
    d1[key] = d[key]

for i,j in d.items():
    occuracnce_list.append(j)
occuracnce_list_sorted = []
occuracnce_list_sorted = sorted(occuracnce_list,reverse=True) 
#print(occuracnce_list_sorted)

    
count = 0
for j in occuracnce_list_sorted:
    for key,val in d1.items():
        if(val == j and count < 3):
            print(key,val)
            d1.pop(key)
            count += 1
            break;

