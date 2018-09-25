'''
https://www.hackerrank.com/challenges/word-order/problem

'''
from collections import OrderedDict
n = int(input())
l= []
for i  in range(n):
    l.append( input())
s = set(l)

print(len(s))

d = OrderedDict()
for i in l:
    if i not in (d):
        d[i] = 1
    else:
        d[i] += 1
l1 = []
l2= []
 
for j,k in d.items():
    l1.append(str(k))
 
print(' '.join(l1))

'''
input:
4
bcdef
abcdefg
bcde
bcdef

output:
3
2 1 1
'''
