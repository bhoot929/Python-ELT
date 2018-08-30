l = [1,[2,[3,[4,[5,2]]]]]

def sumtree(l):
    total = 0
    for x in l:
        if not isinstance(x,list):
            total = total+x
        else:
            total = total + sumtree(x)
    return total


print(sumtree(l))

#Ans:17
