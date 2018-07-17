# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

import random

numbers = [random.randint(1, 1000) for _ in range(10)]
check = True
for el in numbers:
    k = 0
    for i in range(1, el+1):
        k += i
    if k != el * (el + 1) / 2:
        check = False
        break
if check:
    print('Равенство верно!')
else:
    print('Упс, ошибочка')