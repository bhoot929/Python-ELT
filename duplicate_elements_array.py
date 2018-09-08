'''
this code will find duplicate elements from List'''

''first method is normal method where I use two list to store data''

l = [1,2,3,4,4,5,5,6,1]

unique_list = []
duplicate_list = []

for i in l:
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicate_list.append(i)

print(duplicate_list)

'''the same problem can be solved by using Set method''

s = set([x for x in l if l.count(x) > 1])

print(s)
