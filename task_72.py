# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
import random


SIZE = 10
array = [round(random.random() * 50, 2) for _ in range(SIZE)]
print(array)


def merge(left, right):
    sorted_ = []
    left_ind = 0
    right_ind = 0
    left_len = len(left)
    right_len = len(right)
    for _ in range(left_len + right_len):
        if left_ind < left_len and right_ind < right_len:
            if left[left_ind] <= right[right_ind]:
                sorted_.append(left[left_ind])
                left_ind += 1
            else:
                sorted_.append(right[right_ind])
                right_ind += 1
        elif left_ind == left_len:
            sorted_.append(right[right_ind])
            right_ind += 1
        elif right_ind == right_len:
            sorted_.append(left[left_ind])
            left_ind += 1
    return sorted_


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


array = merge_sort(array)
print(array)
