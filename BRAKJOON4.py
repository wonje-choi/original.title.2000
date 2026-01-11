
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(numbers.count(v))


N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for num in numbers:
    if num < X:
        print(num, end=' ')

N = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))


numbers = []
for _ in range(9):
    numbers.append(int(input()))

max_value = max(numbers)
max_index = numbers.index(max_value) + 1

print(max_value)
print(max_index)


N, M = map(int, input().split())

baskets = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for basket in range(i, j + 1):
        baskets[basket] = k

print(' '.join(map(str, baskets[1:])))


N, M = map(int, input().split())

basket = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)


all_students = set(range(1, 31))

submitted = set(int(input()) for _ in range(28))

not_submitted = sorted(all_students - submitted)

for num in not_submitted:
    print(num)


remainders = set(int(input()) % 42 for _ in range(10))
print(len(remainders))


