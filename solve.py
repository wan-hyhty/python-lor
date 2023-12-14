import math


def check_prime(x):
    if x < 2:
        return False
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    # x = int(input())
    cnt = 0
    for i in range(1,len(a)-1):
        l, r = 0, 0
        for j in range(i):
            l += a[j]
        for k in range(i+1, len(a)):
            r += a[k]
        if check_prime(l) and check_prime(r):
            print(i, end = ' ')
            