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