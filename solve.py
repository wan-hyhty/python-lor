from math import *
a, b, c = map(int, input().split())
# n = int(input())

delta = b**2 - 4*a*c
if (a != 0):
    if delta < 0:
        print("VO NGHIEM")
    elif delta == 0:
        x = -b / (2*a)
        print("{:.2f}".format(x))
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print("{:.2f}".format(x2), "{:.2f}".format(x1))
else:
    if b == 0 and c == 0:
        print("VO SO NGHIEM")
    elif b == 0 and c != 0:
        print("VO NGHIEM")
    elif b != 0:
        print("{:.2f}".format(-c/b))
