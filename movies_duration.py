'''
given a list of tuples of movie watched times, find how  many unique minutes of the movie did the viewer watch e.g. [(0,15),(10,25)]. The viewer watched 25 minutes of the movie

'''

t = [(0, 10), (15, 25), (30, 48) ,(12, 20)]

print(t)

t1 = sorted(t)

print('sorted list')
print(t1)

d = t1[0][1] - t1[0][0]


for i in range(1,len(t1)):

    if(t1[i][0] >= t1[i-1][1]):
        d = d + (t1[i][1] - t1[i][0])

    else:
        d = d + (t1[i][1] - t1[i-1][1] )


print('total duration:')
print(d)

''output: 41'''
