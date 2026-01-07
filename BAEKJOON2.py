
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

