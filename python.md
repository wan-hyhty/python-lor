# print

- Cú pháp print(obj, sep = "", end = "")
  - obj là đối tượng in ra
  - sep là ngăn cách giữa các obj, mặc định là < >
  - end là kí tự khi in hết ra obj, mặc định là <\n>

---

# Kiểu dữ liệu

## int: số nguyên

- Không giới hạn

## float: số thực

- Có giới hạn, lớn hơn giới hạn sẽ là inf, nhỏ hơn giới hạn là 0

---

# Ép kiểu

- Cú pháp: int()

# Toán tử

## Gán

a, b, c = 100, 200, 300

- Hoán vị a, b = b, a

## Toán tử tính toán (hk pit tên)

### /

Chia thập phân

```python
print(300/200)
# output: 1.5
```

### //

Chia lấy phần nguyên

```python
print(300/200)
# output: 1
```

### %

Chia lấy phần thập phân (bỏ phần nguyên)

```python
print(300/200)
#output: 5
```

### \*\* (luỹ thừa)

```python
print(2**4)
#output: 16
```

### Toán tử nào đó

- thay vì `a = a * b` thì có thể `a *= b` (trông sang và có ăn có học đàng hoàng =)))

![image](https://user-images.githubusercontent.com/111769169/231203490-7667e785-d509-4735-affe-85e2f522d10f.png)

## Toán tử so sánh

- Trả kết quả True False

```python
print(100 <= 200)
# True
```

## Toán tử logic

### AND

- Lấy hết
- Bảng chân ái

| A   | B   | A and B |
| --- | --- | ------- |
| T   | T   | T       |
| T   | F   | F       |
| F   | T   | F       |
| F   | F   | F       |

### OR

- Lấy 1 trong 2

| A   | B   | A or B |
| --- | --- | ------ |
| T   | T   | T      |
| T   | F   | T      |
| F   | T   | T      |
| F   | F   | F      |

### NOT

- Phủ định

| A   | not(A) |
| --- | ------ |
| T   | F      |
| F   | T      |

## Toán tử nhận dạng (is, not is)

- Kiểm tra 2 obj có giống nhau không (khác với toán tử `==`) (so sánh giá trị)
- nghĩa là 2 thằng tuy cùng tên Lâm, nhưng 2 thằng là 2 obj khác nhau, có cccd (id) khác nhau (so sánh đối tượng)

## Toán tử thành viên (in, not in)

- Kiểm tra có một kí tự nằm trong một chuỗi không

```python
a = 'abcd'
b = 'a'
print(b in a)
# true
```

# INPUT

- Nhập dữ liệu từ bàn phím (input(prompt))
  prompt: câu dẫn
  ví dụ, thay vì:

```python
print('hello Ê Lấm')
lamE = input()
# Ta có thể như này
lamE = input('hello Lâm Ế')
# output: hello Lâm Ế
```

- Mặc định là input() sẽ đọc vào từ bàn phím là kiểu str và đọc hết một dòng(đọc hết đến khi có enter)

- để nhập các số trên cùng 1 dòng

```python
s = input()             # nhập vào từ bàn phím theo kiểu str
s = s.split()           # cắt chuỗi ta vừa nhập ra (split cắt theo dấu cách < > ), kết quả trả về là list (mảng)
x, y, z = map(int, s)   # ép kiểu của list()
```

- khi đã hiểu rồi ta có thể
```python
s = map(int, input().split())
```

# Các hàm toán học phổ biến
Factorial
gcd(a, b)
comb(n, k) tổ hợp k chập n
round(): tròn (5)
fabs(): giá trị tuyệt đối