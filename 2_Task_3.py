﻿# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести 6843.
import re


number = input('Введите натуральное число: ')
num = re.findall(r'[0-9]', number)
rev = ''
for el in reversed(num):
    rev = rev + el
print(f'Обратное число: {rev}')
