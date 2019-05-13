# Написать два алгоритма нахождения i-го по счёту простого числа.

import cProfile
import timeit

# Используем решето
# если вкратце, мы просеиваем числа до какого-то N, увеличивая это N
# с каждым шагом до того момента, пока на выходе не будет массив нужной нам длины


def sieve1(n):
    result = []
    a = 1
    while len(result) < n:
        a += 1
        sieve = [i for i in range(a)]
        sieve[1] = 0
        for i in range(2, a // 2 + 1):
            if sieve[i] != 0:
                j = i + i
                while j < a:
                    sieve[j] = 0
                    j += i
        result = [i for i in sieve if i != 0]
    return result[-1]
# алгоритм, подозреваю, отвратительный, но у него есть один плюс - он работает.

# Второй вариант - простой и логичный


def sieve2(n):
    a = 1
    k = 0
    while k < n:
        a += 1
        flag = True
        for i in range(2, a//2 + 1):
            if a % i == 0:
                flag = False
        if flag:
            k += 1
    return a

# Оба алгоритма проверены через print и т.д.

# cProfile.run('sieve1(100)')
#          1628 function calls in 0.057 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.057    0.057 <string>:1(<module>)
#         1    0.043    0.043    0.057    0.057 Task_42.py:11(sieve1)
#       541    0.007    0.000    0.007    0.000 Task_42.py:16(<listcomp>)
#       541    0.007    0.000    0.007    0.000 Task_42.py:24(<listcomp>)
#         1    0.000    0.000    0.057    0.057 {built-in method builtins.exec}
#       542    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sieve2(100)')
#          4 function calls in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.008    0.008    0.008    0.008 Task_42.py:31(sieve2)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Уже здесь видно, насколько первый алгоритм не подходит для данной задачи, много ненужных вызовов функций, огромное
# время выполнения, но с ТЗ спорить нельзя.

# первый вариант
# python -m timeit -n 100 -s "import Task_42" "Task_42.sieve1(10)"
# 100 loops, best of 5: 170 usec per loop
# python -m timeit -n 100 -s "import Task_42" "Task_42.sieve1(20)"
# 100 loops, best of 5: 842 usec per loop
# python -m timeit -n 100 -s "import Task_42" "Task_42.sieve1(100)"
# 100 loops, best of 5: 59.5 msec per loop
# что-то мне подсказывает, что здесь даже не квадратичный рост, а еще выше

# второй вариант
# python -m timeit -n 100 -s "import Task_42" "Task_42.sieve2(10)"
# 100 loops, best of 5: 28.9 usec per loop
# python -m timeit -n 100 -s "import Task_42" "Task_42.sieve2(20)"
# 100 loops, best of 5: 124 usec per loop
# python -m timeit -n 100 -s "import Task_42" "Task_42.sieve2(100)"
# 100 loops, best of 5: 5.76 msec per loop
# Понятное дело, что чем выше номер числа, тем ниже частота появления простых чисел, поэтому здесь тоже
# высокая скорость роста, хоть и на порядок ниже, чем в первом варианте

# Выводы:
# 1. В рамках выполненной задачи были написаны две функции для нахождения простого числа по его порядковому
# номеру в ряде простых чисел. Для каждой функции были посчитаны времена выполнения для трех аргументов (10, 20, 100).
# На основе полученных данным были сделаны выводы о характере роста времени выполнения относительно аргумента.
# 2. Безусловно, в рамках решаемой задачи, второй метод является оптимальным, как по объему кода, так и по времени
# выполнения.
