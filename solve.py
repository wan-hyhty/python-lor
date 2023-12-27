import math


def check_prime(a):
    a.append(0)
    a.append(1)

    i = 2
    while a[i-2] <= 10e18:
        a.append(a[i - 1] + a[i - 2])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    max, min = 0, 1e7
    max_idx, min_idx = 0, 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            max_idx = i
        if a[i] <= min:
            min = a[i]
            min_idx = i
    print(min_idx, max_idx, end = ' ')
