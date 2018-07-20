# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

list_ran = [random.randint(1, 100) for _ in range(20)]
print(list_ran)
max_list = max(list_ran)
min_list = min(list_ran)
id_max = list_ran.index(max_list)
id_min = list_ran.index(min_list)
list_ran.insert(id_min, max_list)
list_ran.pop(id_min + 1)
list_ran.insert(id_max, min_list)
list_ran.pop(id_max + 1)
print(list_ran)
