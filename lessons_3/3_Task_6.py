# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random


list_ran = [random.randint(-5, 5) for _ in range(5)]
print(list_ran)
max_num = max(list_ran)
min_num = min(list_ran)
place_1 = list_ran.index(max_num)
place_2 = list_ran.index(min_num)
if place_1 > place_2:
    place_1, place_2 = place_2, place_1
sum_list = sum(list_ran[place_1 + 1: place_2])
print(f'Сумма равна:{sum_list}')
