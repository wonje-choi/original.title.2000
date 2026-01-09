
N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)

n = int(input())
print(n * (n + 1) // 2)


X = int(input())
N = int(input())

total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

if total == X:
    print("Yes")
else:
    print("No")

N = int(input())
print("long " * (N // 4) + "int")

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)

import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A + B}")

import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A + B}")

N = int(input())
for i in range(1, N + 1):
    print('*' * i)

N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)

