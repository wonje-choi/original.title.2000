
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("     |")
print("     |")


a, b, c, d, e, f = map(int, input().split())
print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)


n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))


s = input()
print(1 if s == s[::-1] else 0)


s = input().upper()
counts = [0] * 26

for c in s:
    counts[ord(c) - ord('A')] += 1

max_count = max(counts)

if counts.count(max_count) > 1:
    print('?')
else:
    print(chr(counts.index(max_count) + ord('A')))


s = input()
croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for c in croatia:
    s = s.replace(c, '*')

print(len(s))


