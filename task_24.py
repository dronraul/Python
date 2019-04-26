# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def amount(a):
    k = 0
    for j in a:
        k += int(j)
    return k


maxi = 0
n = int(input("сколько чисел вы хотите ввести"))
for i in range(0, n):
    d = input()
    if amount(d) > maxi:
        z = d
        maxi = amount(d)
print("это число ", z, "сумма его цифр ", maxi)

