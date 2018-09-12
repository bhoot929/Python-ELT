'''
This code will group the string and print occurances

Example:
1222311

output:
(1, 1) (3, 2) (1, 3) (2, 1)

'''
s = '1222311'

from itertools import groupby

for k,c in groupby(s):
    print(k,list(c))
    print(k,len(list(c)))

print(*[(len(list(c)),int(k)) for k,c in groupby(s)])

output:

(1, 1) (3, 2) (1, 3) (2, 1)
