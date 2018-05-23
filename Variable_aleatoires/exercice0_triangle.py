# Algorithme

N = 10
triangle = [[0]*N for _ in range(N)]

triangle[0][0] = 1

for i in range(1, N):
    triangle[i][0] = 1
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle[i][i] = 1

print(triangle)