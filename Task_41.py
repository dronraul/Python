# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import cProfile
import timeit


# первый способ - через сумму ряда циклом


def met1(n):
    a = 1
    s = 0
    for i in range(0, n):
        s += a
        a *= (-0.5)
    return s

# второй способ - через сумму прогрессии


def met2(n):
    f = (1-(-0.5)**n)/1.5
    return f


# третий способ - заполняем массив и находим его сумму


def met3(n):
    m = [1]
    a = 1
    for i in range(1, n):
        a *= (-0.5)
        m += [a]
    s = sum(m)
    return s


# _____________1 вариант cProfile


# cProfile.run('met1(100)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_41.py:11(met1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('met2(100)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_41.py:22(met2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('met3(100)')
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_41.py:30(met3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Особо никакой разницы, кроме того, что в третьем методе вызывается 5 функций. Что и ожидалось.

# ____________2 вариант timeit
# met1
# python -m timeit -n 100 -s "import Task_41" "Task_41.met1(10)"
# 100 loops, best of 5: 1.58 usec per loop
# >python -m timeit -n 100 -s "import Task_41" "Task_41.met1(20)"
# 100 loops, best of 5: 2.98 usec per loop
# python -m timeit -n 100 -s "import Task_41" "Task_41.met1(50)"
# 100 loops, best of 5: 6.3 usec per loop
# python -m timeit -n 100 -s "import Task_41" "Task_41.met1(100)"
# 100 loops, best of 5: 12.1 usec per loop
# я построил график, получилась линейная зависимость, т.е. можно сделать вывод о линейном порядке роста

# met2
# python -m timeit -n 100 -s "import Task_41" "Task_41.met2(10)"
# 100 loops, best of 5: 612 nsec per loop
# python -m timeit -n 100 -s "import Task_41" "Task_41.met2(20)"
# 100 loops, best of 5: 604 nsec per loop
# python -m timeit -n 100 -s "import Task_41" "Task_41.met2(100)"
# 100 loops, best of 5: 596 nsec per loop
# классический вариант константного порядка роста, что вполне себе математически логично

# met3
# python -m timeit -n 100 -s "import Task_41" "Task_41.met3(10)"
# 100 loops, best of 5: 2.76 usec per loop
# python -m timeit -n 100 -s "import Task_41" "Task_41.met3(20)"
# 100 loops, best of 5: 4.47 usec per loop
# python -m timeit -n 100 -s "import Task_41" "Task_41.met3(100)"
# 100 loops, best of 5: 17.6 usec per loop
# И снова линейный порядок роста.

# Выводы:
# 1. В рамках выполненной задачи были написаны три функции для нахождения суммы поледовательности, описанной
# перечислением. Для каждой функции были посчитаны времена выполнения для трех аргументов (10, 20, 100). На основе
# полученных данным были сделаны выводы о характере роста времени выполнения относительно аргумента.
# 2. Безусловно, в рамках решаемой задачи, второй метод является оптимальным, как по объему кода, так и по времени
# выполнения. Увеличение аргумента у функции никак не влияет на время выполнения, что тоже является несомненным плюсом.
# Однако, стоит заметить, что в третьем методе мы имеем возможность получить гораздо больше информации в процессе
# выполнения, так как заполняем массив данными. Это может быть полезно для оперативного изменения решения задачи
# при резком изменении ТЗ по прихоти заказчика.
