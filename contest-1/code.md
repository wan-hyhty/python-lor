# Bài 1. Tính toán giá trị của biểu thức

```python
# x, y, z, t = map(int, input().split())

x = int(input())

y = x ** 3 + 3 * x ** 2 + x + 1
print(y)
```

# Bài 2. Tính toán giá trị biểu thức 2

```python
x, y, z = map(int, input().split())
# x = int(input())

S = x * (y + z) + y*(x + z)
print(S)
```

# Bài 3. Đổi nhiệt độ

```python
# x, y, z = map(int, input().split())
x = int(input())

F = (x * 9 /5) + 32
print("{:.2f}".format(F))
```

# Bài 4. Chu vi và diện tích hình tròn

```python
# x, y, z = map(int, input().split())
x = int(input())
pi = 3.14

C = 2 * pi * x
S = pi * x ** 2
print("{:.4f}".format(C), "{:.4f}".format(S))
```

# Bài 5. Khoảng cách Euclid.

```python
from math import *
x1, y1, x2, y2 = map(int, input().split())
# x = int(input())

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("{:.2f}".format(d))
```

# Bài 6. Luyện tập viết câu điều kiện

```python
from math import *
# x1, y1, x2, y2 = map(int, input().split())
n = int(input())

# 1
if (n % 2 == 0):
    print("YES")
else:
    print("NO")
# 2
if ((n % 3 == 0) and (n % 5 == 0)):
    print("YES")
else:
    print("NO")

# 3
if (n % 3 == 0 and n % 7 != 0):
    print("YES")
else:
    print("NO")

# 4
if (n % 3 == 0 or n % 7 == 0):
    print("YES")
else:
    print("NO")

# 5
if (n > 30 and n < 50):
    print("YES")
else:
    print("NO")

# 6
if (n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0)):
    print('YES')
else:
    print('NO')

# 7
r = n % 10
if (n >= 10) and (n <= 99) and (r == 2 or r == 3 or r == 5 or r == 7):
    print('YES')
else:
    print('NO')

#8
if(n <= 100 and n % 23 == 0):
    print("YES")
else:
    print("NO")

#9
if(n < 10 or n > 20):
    print('YES')
else:
    print('NO')

#10
if( r % 3 == 0):
    print('YES')
else:
    print('NO')
```

# Bài 7. Số lớn nhất và nhỏ nhất

```python
from math import *
x, y = map(int, input().split())
# n = int(input())

print(x//y * y)
print((x + y - 1) // y * y)
```

# Bài 8. Tổng, hiệu, tích, thương

```python
from math import *
x, y = map(int, input().split())
# n = int(input())

print(x + y, x - y, x * y, sep = "\n")
if (y == 0):
    print('INVALID')
else:
    print("{:.4f}".format(x / y))
```

# Bài 9.Kiểm tra năm nhuận

```python
from math import *
# x, y = map(int, input().split())
n = int(input())

if ( (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)):
    print("YES")
else:
    print('NO')
```

# Bài 10. Tam giác hợp lệ

```python
from math import *
x, y, z = map(int, input().split())
# n = int(input())

if(x >= 0 and y >= 0 and z >= 0):
    if(x + y > z and x + z > y and y + z > x):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
```

```python
from math import *
x, y, z = map(int, input().split())
# n = int(input())


def main():
    if (x >= 0 and y >= 0 and z >= 0):
        if (x + y > z and x + z > y and y + z > x):
            print('YES')
            return
    print('NO')


main()
```

# Bài 11. Kiểm tra tam giác

```python
from math import *
x, y, z = map(int, input().split())
# n = int(input())

if (x > 0 and y > 0 and z > 0 and x + y > z and x + z > y and y + z > x):
    if (x == y and x == z):
        print('1')
    elif (x == y or x == z or z == y):
        print('2')
    elif(x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2):
        print('3')
    else:
        print("4")
else:
    print("INVALID")
```

# Bài 12. Số ngày của tháng

```python
from math import *
n, m = map(int, input().split())
# n = int(input())
if (n >= 1 and n <= 12 and m > 0):
    if (n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12):
        print(31)
    elif(n == 4 or n == 6 or n == 9 or n == 11):
        print(30)
    else:
        if (m % 400 == 0) or (m % 4 == 0 and m % 100 != 0):
            print(29)
        else:
            print(28)
else:
    print("INVALID")
```

# Bài 13. Đổi ngày sang năm, tuần, ngày

```python
from math import *
# n, m = map(int, input().split())
n = int(input())

y, w = 0, 0
if n >= 365:
    y = n // 365
    n -= y*365

if (n >= 0):
    w = n // 7
    n -= w * 7

print(y, w, n)
```

# Bài 14. Xếp loại học sinh

```python
from math import *
x, y, z, t = map(float, input().split())
# n = int(input())

dtb = (x + y + z * 2 + t * 3) / 7

if(dtb >= 8): print("GIOI")
elif(dtb >= 6.5): print('KHA')
elif(dtb >= 5): print('TRUNG BINH')
else: print('YEU')
```

# Bài 15. Mua nước

```python
from math import *
n, a, b = map(int, input().split())
# n = int(input())

if a * 2 <= b:
    print(n * a)
else:
    if (n % 2 == 0):
        print(n // 2 * b)
    else:
        print(n // 2 * b + a)
```

# Bài 16. Kí tự kế tiếp

```python
from math import *
# n, a, b = map(int, input().split())
n = input()

if (n >= 'A' and n <= 'Y'):
    print(chr(ord(n) + 33))
elif (n >= 'a' and n <= 'y'):
    print(chr(ord(n) + 1))
elif (n == 'Z'):
    print(chr(ord(n) + 7))
else:
    print(chr(ord(n) - 25))
```

# Bài 17:

```python
from math import *
# n, a, b = map(int, input().split())
n = input()

if n.islower():
    print('LOWER')
elif n.isupper():
    print('UPPER')
elif n.isdigit():
    print('DIGIT')
else:
    print('SPECIAL')
```

# Bài 18. Chuyển đổi in hoa in thường

```python
from math import *
# n, a, b = map(int, input().split())
n = input()

if n >= 'a' and n <= 'z':
    print(chr(ord(n) - 32))
elif n >= 'A' and n <= 'Z':
    print(chr(ord(n) + 32))
else:
    print(n)
```

```python
from math import *
# n, a, b = map(int, input().split())
n = input()

if n >= 'a' and n <= 'z':
    print(n.upper())
elif n >= 'A' and n <= 'Z':
    print(n.lower())
else:
    print(n)
```

# Bài 19. Domino

```python
from math import *
m, n = map(int, input().split())
# n = input()

if (m % 2 == 0):
    print(m // 2 * n)
else:
    print(m // 2 * n + n // 2)
```

# Bài 20. Lát đá quảng trường

```python
from math import *
n, m, a = map(int, input().split())
# n = input()

size = ceil(n / a) * ceil(m / a)
print(size)
```

# Bài 21. Frog

```python
from math import *
a, b, k = map(int, input().split())

if(k % 2 == 0):
    print(a * (k//2) - b * (k//2))
else:
    print(a * (k//2 + 1) - b * (k//2))
```

# Bài 22. Đồng xu

```python
from math import *
n, s = map(int, input().split())

print(ceil(s/n))
```

# Bài 24. Đường đi ngắn nhất

```python
from math import *
d1, d2, d3 = map(int, input().split())
sum_d1_d3_d2 = d1 + d3 + d2
sum_d1_d1_d2_d2 = d1*2 + d2*2
sum_d1_d3_d3_d1 = d1*2 + d3*2
sum_d2_d3_d3_d2 = d2*2 + d3 * 2
print(min(sum_d1_d3_d2, sum_d1_d3_d3_d1, sum_d1_d1_d2_d2, sum_d2_d3_d3_d2))
```

# Bài 25. Đổi tiền

```python
from math import *
# d1, d2, d3 = map(int, input().split())
n = int(input())
count = 0
if (n >= 100):
    count += n // 100
    n -= (n // 100) * 100
if n >= 20:
    count += n // 20
    n -= (n // 20) * 20
if n >= 10:
    count += n // 10
    n -= (n // 10) * 10
if n >= 5:
    count += n // 5
    n -= (n // 5) * 5
if n >= 1:
    count += n // 1
    n -= (n // 1) * 1
print(count)
```

# Bài 26. Số lớn nhất nhỏ nhất trong 4 số

```python
from math import *
a, b, c, d = map(int, input().split())

print(max(a, b, c, d), min(a, b, c, d))
```

# Bài 27. Làm tròn số

```python
from math import *
# a, b, c, = map(int, input().split())
n = float(input())

print(round(n))
```

# Bài 28. Cấp số cộng

```python
from math import *
n, u1, d = map(int, input().split())
# n = float(input())

un = u1 + (n - 1) * d
s = (n / 2) * (u1 + un)
print(int(s))
```

# Bài 29. Cấp số nhân

```python
from math import *
a, b, c, d = map(int, input().split())
# n = float(input())
def main():
    x = b//a
    if( b * x == c):
        if(c * x == d):
            print("YES")
            return 0
    print("NO")

if __name__ == main():
    main()
```

# Bài 30. Tổ hợp chập 2

```python
from math import *
# = map(int, input().split())
n = int(input())

print(comb(n, 2))
```

# Bài 31. Bizon the Champion

```python
from math import *
a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())

x = ceil((a1 + a2 + a3) / 5)
y = ceil((b1 + b2 + b3) / 10)
if(x + y <= n):
    print("YES")
else:
    print("NO")
```

# Bài 32. Ghép số

```python
from math import *
k2, k3, k5, k6 = map(int, input().split())
# n = int(input())


x = min(k2, k5, k6)
k2 -= x
sum = 256 * x
if k2 > 0:
    y = min(k2, k3)
    sum += 32 * y
print(sum)
```

# Bài 33. Chia tiền

```python
from math import *
a, b, c, n = map(int, input().split())
# n = int(input())


x = max(a, b, c)
if a <= x:
    n -= (x - a)
if b <= x:
    n -= (x - b)
if c <= x:
    n -= (x - c)
if n >= 0:
    if (n % 3 == 0):
        print("YES")
    else:
        print("NO")
else:
    print('NO')
```

# Bài 34. Sự hào phóng

```python
from math import *
a, b, c, d, e = map(int, input().split())
# n = int(input())


avg = a + b + c+d + e
if avg % 5 == 0:
    temp = avg // 5
    if temp != 0:
        print(temp)
    else:
        print(-1)
else:
    print(-1)
```

# Bài 35. HPNY

```python
from math import *
h, m = map(int, input().split())
# n = int(input())

time_m = 60 - m
time_h = 24 - (h + 1)

print(time_h * 60 + time_m)
```

# Problem E

```python
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
```