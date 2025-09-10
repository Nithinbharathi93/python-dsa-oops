m, n = map(int, input().split())
mat = [[1]*m for i in range(n)]
mat[0][0] = 0
print(mat)

for i in range(1, m):
    for j in range(1, n):
        mat[i][j] = mat[i][j-1] + mat[i-1][j]

for i in range(m):
    print(*mat[i])