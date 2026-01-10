
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