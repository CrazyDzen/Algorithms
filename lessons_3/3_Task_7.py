# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.
import random

list_ran = [random.randint(-20, 20) for _ in range(10)]
min_num = min(list_ran)
list_copy = list_ran.copy()
list_copy.remove(min_num)
min_num_2 = min(list_copy)
print(f'Два наименьших числа:{min_num}, {min_num_2}')
