# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.

import hashlib

s = input('введите слово  ')


def search(a):
    k = []
    for i in range(0, len(a)+1):
        for j in range(i, len(a)+1):
            if (a[i:j] != '') and (a[i:j] != a):
                l = hashlib.sha1(a[i:j].encode('utf-8')).hexdigest()
                if not (l in k):
                    k.append(l)
    return len(k)


kol = search(s)
print(kol)
