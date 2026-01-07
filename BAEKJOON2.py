
A, B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

H, M = map(int, input().split())

M -= 45

if M < 0:
    M += 60
    H -= 1
    if H < 0:
        H = 23

print(H, M)

H, M = map(int, input().split())
C = int(input())

total_minutes = H * 60 + M + C

H = (total_minutes // 60) % 24
M = total_minutes % 60

print(H, M)

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + a * 100)
else:
    print(max(a, b, c) * 100)