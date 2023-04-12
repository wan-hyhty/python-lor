from math import *
n, m, a = map(int, input().split())
# n = input()

size = ceil(n / a) * ceil(m / a)
print(size)
