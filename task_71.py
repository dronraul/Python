# Отсортируйте по убыванию методом пузырька одномерный
# целочисленный массив, заданный случайными числами на промежутке [-100; 100)

import random
SIZE = 10
array = [random.randint(-100, 99) for _ in range(SIZE)]
print(array)


def bub(arr):
    for i in range(len(arr) - 1):
        f = True
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                f = False
        if f is True:
            break


bub(array)
print(array)