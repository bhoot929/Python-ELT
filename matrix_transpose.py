

matrix =[[1,2,3,4],
        [6,7,8,9],
        [11,12,13,14],
        [16,17,18,19]]


l = len(matrix)
print(matrix)

for i in range(l):
        for j in range(l):
            if(i!=j):
                matrix[i][j] =  matrix[j][i]


print(matrix)

''' output:
[[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14], [16, 17, 18, 19]]
[[1, 6, 11, 16], [6, 7, 12, 17], [11, 12, 13, 18], [16, 17, 18, 19]]'''
