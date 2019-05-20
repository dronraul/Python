# Во втором массиве сохранить индексы четных элементов первого массива.
import random
array = [random.randint(0, 100) for _ in range(10)]
print(array)
a = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        a += [i+1]
print(a)