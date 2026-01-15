
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


def is_group_word(word):
    seen = set()
    prev = ''
    
    for char in word:
        if char != prev:
            if char in seen:
                return False
            seen.add(char)
        prev = char
    
    return True

n = int(input())
count = 0

for _ in range(n):
    word = input()
    if is_group_word(word):
        count += 1

print(count)


gp = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
tc = ts = 0

for _ in range(20):
    _, c, g = input().split()
    if g != 'P':
        tc += float(c)
        ts += float(c) * gp[g]

print(ts / tc)