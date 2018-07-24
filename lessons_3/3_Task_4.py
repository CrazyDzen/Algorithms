# Определить, какое число в массиве встречается чаще всего
import random

list_ran = [random.randint(1, 10) for _ in range(20)]
print(list_ran)
most = 0
num = 0
for i in range(len(list_ran)):
    k = 0
    for j in range(i+1, len(list_ran)):
        if list_ran[i] == list_ran[j]:
            k += 1
    if k > most:
        most = k
        num = list_ran[i]
print(f'Число {num} встречается {most} раз')
