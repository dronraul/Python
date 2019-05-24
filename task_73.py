# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
import random
SIZE = int(input('введите M '))
# На числа ограничений не было, значит будет от 1 до 100
array = [random.randint(1, 100) for _ in range(2*SIZE + 1)]
print(array)


def medi(arr):
    for i in range(0, SIZE):
        arr.remove(min(arr))
    for i in range(0, SIZE):
        arr.remove(max(arr))
    return arr[0]


b = medi(array)
print('медиана равна ', b)

