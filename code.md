# Mục lục

# Bài 1. Print Hello World

```python
a = input()
print(a, 'Hello World !', '28tech C++ programming !', sep = "\n")
```

# Bài 2. Print number

```python
a = int(input())
b = int(input())
c = input()
d = float(input())
e = float(input())
print(a, b, c,"{:.2f}".format(d),"{:.9f}".format(e), sep = '\n')
```

```python
a, b, c, d, e = int(input()), int(input()), input(), float(input()), float(input())
print(a, b,c, "{:.2f}".format(d), "{:.9f}".format(e), sep = "\n")
```

# Bài 3. Print expression

```python
x, y, z, t = map(int, input().split())
print(y, z, x, t, sep=",")
print(x + y + z + t)
print(x - y + z * t)
```

# Bài 4. Hàm pow

```python
x, y = map(int, input().split())
print(x ** y)
```

```python
x, y = map(int, input().split())
print(pow(x, y))
```

# Bài 5. Hàm sqrt và cbrt

```python
from math import *
x = int(input())
print("{:.2f}".format(sqrt(x)))
print("{:.3f}".format(pow(x, 1/3)))
```

# Bài 6. Hàm ceil, floor, round

```python
from math import *
x = float(input())
print(floor(x), ceil(x),  round(x), sep="\n")
```

# Bài 7. Chữ số cuối cùng và 2 chữ số cuối cùng

```python
x = int(input())

print(x % 10)
print(x % 100)
```

# Bài 8. Phép chia

```python
a, b = map(int, input().split())

print(b // a)
print("{:.2f}".format(b/a))
```

# Bài 9. Xóa số

```python
a = int(input())

print(a // 1000)
```

# Bài 10. Phép chia dư

```python
a, b = map(int, input().split())

print(a % b)
```

# Bài 11. Nhân chia

```python
# a = map(int, input().split())
a = int(input())

print(a*2, end="\n\n")
print(a*10, end="\n\n")
print(a//2, end="\n\n")
print("{:.3f}".format(a/2))
```

# Bài 12. Hàm F(x, y)

```python
x, y = map(int, input().split())
# a = int(input())

f = 5 * x + 2 * y + x * y

print(f)
```

# Bài 13. Lớn nhất, nhỏ nhất
```python
# x, y, z, t = map(int, input().split())
# a = int(input())

x = int(input())
y = int(input())
z = int(input())
t = int(input())

print(max(x, y))
print(min(z, t))
print(max(x, y ,z))
print(min(x, y, z, t))
```

# Bài 14. Number in range
```python
x, y = map(int, input().split())
# a = int(input())

print(y - x + 1)
```

# Bài 15. Mua vở
```python
x, y = map(int, input().split())

print(f"SO VO MUA DUOC LA : {x // y} !!!!!")
```

# Bài 16. Cout
```python
x, y, z, t = map(int, input().split())

print(x, y, z, t, sep='  ', end="\n\n")
print(y, z, x, t, sep='--', end="\n\n")
print(2 * x, 3 * y, 4 * z, 5 * t, sep=',', end="\n\n")
print("KET THUC !!")
```