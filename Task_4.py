﻿# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


import random


action = input('Выберите действие:'
               '\nВведите 1 - если необходимо случайное целое число;'
               '\nВведите 2 - если необходимо случайное вещественное число;'
               '\nВведите 3 - если необходим случайный символ.'
               '\n: ')
enter_span = input('Введите требуемый диапазон через запятую: ')
span = enter_span.split(',')
if action == '1':
    answer = random.randint(int(span[0]), int(span[1]))
elif action == '2':
    answer = random.uniform(float(span[0]), float(span[1]))
elif action == '3':
    letters = list(map(chr, range(ord(span[0]), ord(span[1])+1)))
    n = random.randint(0, len(letters) - 1)
    answer = letters[n]
print(answer)


