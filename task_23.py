# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
n = int(input("введите количество элементов ряда  "))
a = 1
s = 0
for i in range(0, n):
    s += a
    a *= (-0.5)
print(s)
