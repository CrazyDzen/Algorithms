﻿# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125… Количество элементов
# (n) вводится с клавиатуры.


n = int(input('Введите число элементов: '))
sum = 1
k = 1
for i in range(1, n):
    sum += k / (-2)
    k = k / (-2)
print(sum)