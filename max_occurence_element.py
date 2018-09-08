'''
this code will get maximum occurence element in list
'''

l = [1,2,3,4,4,5,5,5,6,1]

max_count = 0
element = l[0]
for i in l:

    if(l.count(i)>max_count):
        max_count = l.count(i)
        element = i


print(str(element)+' - '+str(max_count))
