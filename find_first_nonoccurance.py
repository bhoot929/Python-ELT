''this code will find first non-occurance element in list'''

l = [1,2,3,4,4,5,5,6,1]

len_l = len(l)
non_req = ''

for i in range(len_l):
    new_l = l[i+1:]
    if (l[i] not in new_l):
        print(l[i])
         
        break;
    
