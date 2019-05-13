# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
array[x], array[y] = array[y], array[x]
print(array)
