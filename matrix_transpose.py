'''
3*3 matrix will convert to 3*3
4*3 matrix will convert to 3*4
'''

matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]


length = len(matrix)
breath = len(matrix[0])

print('length:',length)
print('\n')
print('breath:',breath)
print('\n')

new_m = [[0 for i in range(length)] for j in range(breath)]



for i in range(breath):
    for j in range(length):

            new_m[i][j] = matrix[j][i]

print(new_m)
