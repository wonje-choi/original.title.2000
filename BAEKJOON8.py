
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


T = int(input())
for _ in range(T):
    C = int(input())
    
    quarter = C // 25
    C %= 25
    
    dime = C // 10
    C %= 10
    
    nickel = C // 5
    C %= 5
    
    penny = C
    
    print(quarter, dime, nickel, penny)


