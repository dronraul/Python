# Написать программу сложения и умножения двух шестнадцатеричных чисел.

from collections import deque


n = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
     '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
     'D': 13, 'E': 14, 'F': 15}
a = []
b = []
k = input('введите первое число   ')
for char in k:
   a.append(char)
print(a)
k = input('введите второе число   ')
for char in k:
   b.append(char)
k = 0
p = 0
a.reverse()
b.reverse()
k1 = 0
for i in range(0, len(a)):
    k1 += n[a[i]]*16**i
k2 = 0
for i in range(0, len(b)):
    k2 += n[b[i]]*16**i
k3 = k1 + k2
k4 = k1 * k2
s = deque()
p = deque()

res = {value: key for key, value in n.items()}
print(k3)
print(k4)
while k3 > 0:
    t = k3 % 16
    s.appendleft(res[t])
    k3 = k3 // 16
while k4 > 0:
    t = k4 % 16
    p.appendleft(res[t])
    k4 = k4 // 16
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
# ответ представлен в том же виде, что и в ТЗ
print('сумма чисел   ', s)
print('произведение чисел   ', p)
