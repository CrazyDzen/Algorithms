# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве.
import random

list_ran = [random.randint(-50, 50) for _ in range(20)]
print(list_ran)
num = min(list_ran)
if num < 0:
    print(f'Наибольшее отрицательное число {num}'
          f'\nпозиция - {list_ran.index(num)}')
else:
    print('В массиве нет отрицательных чисел')
