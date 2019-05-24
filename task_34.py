# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
array = [random.randint(0, 100) for _ in range(10)]
print(array)
mini = array[0]
maxi = array[0]
x = 0
y = 0
for i in range(len(array)):
    if array[i] > maxi:
        maxi = array[i]
        x = i
    if array[i] < mini:
        mini = array[i]
        y = i
if x > y:
    x, y = y, x
sum_ = 0
for i in range(x + 1, y):
    sum_ += array[i]
print(sum_)
