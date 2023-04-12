from math import *
# n, a, b = map(int, input().split())
n = input()

if (n >= 'A' and n <= 'Z'):
    print('UPPER')
elif n >= 'a' and n <= 'z':
    print('LOWER')
elif n >= '0' and n <= '9':
    print('DIGIT')
else:
    print('SEPCIAL')
