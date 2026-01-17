
n, b = input().split()
b = int(b)

result = 0
for i, char in enumerate(reversed(n)):
    if char.isdigit():
        digit = int(char)
    else:
        digit = ord(char) - ord('A') + 10
    
    result += digit * (b ** i)

print(result)


n, b = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ''
while n > 0:
    result = digits[n % b] + result
    n //= b

print(result)


