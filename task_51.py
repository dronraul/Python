# ользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 ...
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

firm = namedtuple('firm', 'name, aver')
ent = []
s = 0
N = int(input('введите количество предприятий   '))
for i in range(0, N):
    name = input('введите название предприятия   ')
    kv1 = int(input('прибыль за 1 квартал   '))
    kv2 = int(input('прибыль за 2 квартал   '))
    kv3 = int(input('прибыль за 3 квартал   '))
    kv4 = int(input('прибыль за 4 квартал   '))
    aver = (kv1 + kv2 + kv3 + kv4) / 4
    s += aver/N
    comp = firm(name, aver)
    ent.append(comp)

for i in range(0, N):
    print('средняя прибыль компании ', ent[i].name, ' равна ', ent[i].aver)
print('следующие предприятия заработали выше среднего по рынку')
for i in range(0, N):
    if ent[i].aver > s:
        print(ent[i].name)
print('следующие предприятия заработали ниже среднего по рынку')
for i in range(0, N):
    if ent[i].aver < s:
        print(ent[i].name)

