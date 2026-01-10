
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

