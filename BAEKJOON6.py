
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("     |")
# print("     |")


# a, b, c, d, e, f = map(int, input().split())
# print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)


n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))