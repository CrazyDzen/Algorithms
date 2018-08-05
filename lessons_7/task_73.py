# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.
from random import randint


def median(list):
    for el in list:
        more = 0
        less = 0
        for els in list:
            if el > els:
                less += 1
            elif el < els:
                more += 1
        if more == less:
            return el
    return 'fuck'


my_list = [randint(-100, 99) for _ in range(11)]
print(my_list)
print(median(my_list))
