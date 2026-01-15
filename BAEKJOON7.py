
n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(' '.join(str(A[i][j] + B[i][j]) for j in range(m)))


max_val = -1
max_row, max_col = 0, 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_val:
            max_val = row[j]
            max_row = i + 1
            max_col = j + 1

print(max_val)
print(max_row, max_col)


lines = [input() for _ in range(5)]
max_len = max(len(line) for line in lines)

result = ''
for col in range(max_len):
    for row in range(5):
        if col < len(lines[row]):
            result += lines[row][col]

print(result)