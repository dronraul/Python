# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
array = [random.randint(-100, 100) for _ in range(10)]
mini = float('-inf')  # не уверен, что это оптимальнее всего, но ничего умнее не нарыл
print(array)
for i in range(len(array)):
    if (array[i] > mini) and (array[i] < 0):
        mini = array[i]
        x = i
if mini == float('-inf'):
    print('отрицательных элементов нет')  # один из 1024 случаев, но вдруг
else:
    print('максимальный отрицательный элемент равен ', mini, 'его позиция ', x+1)
# Наверное, пользователю все-таки удобнее считать не с нуля


