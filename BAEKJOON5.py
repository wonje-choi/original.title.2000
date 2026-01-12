
S = input()
i = int(input())
print(S[i-1])


word = input()
print(len(word))


T = int(input())
for _ in range(T):
    S = input()
    print(S[0] + S[-1])


c = input()
print(ord(c))


N = int(input())
S = input()
print(sum(map(int, S)))


S = input()
result = [S.find(chr(i)) for i in range(ord('a'), ord('z')+1)]
print(*result)


