
n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(' '.join(str(A[i][j] + B[i][j]) for j in range(m)))


