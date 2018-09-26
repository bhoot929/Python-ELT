# this code will fill string in emtpy space in a setence:


def join(word,replace):
    l = list()
    for i in range(len(word)):
        if(word[i] == ' '):
            l.append(replace)
        else:
            l.append(word[i])
    return ''.join(l)
print(join('Join the Stack Overflow Community' , '%20'))

'''
output:Join%20the%20Stack%20Overflow%20Community
'''
 
