# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(-20, 20) for _ in range(5)] for _ in range(5)]
min_numbers = [min(el) for el in matrix]
print(max(min_numbers))
