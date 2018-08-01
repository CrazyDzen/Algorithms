import random
from sys import getsizeof as size

# python 3.6 windows8x64

# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.


series = [random.randint(0, 100) for _ in range(10)]
least = min(series)
series_copy = series.copy()
series_copy.remove(least)
least_2 = min(series_copy)
print(f'Два наименьших числа:{least}, {least_2}')

'''
variable: [12, 4, 100, 73, 64, 65, 72, 17, 66, 37], type: <class 'list'>, id:9924520, size: 100
    variable: 12, type: <class 'int'>, id:1747968960, size: 14
    variable: 4, type: <class 'int'>, id:1747968832, size: 14
    variable: 100, type: <class 'int'>, id:1747970368, size: 14
    variable: 73, type: <class 'int'>, id:1747969936, size: 14
    variable: 64, type: <class 'int'>, id:1747969792, size: 14
    variable: 65, type: <class 'int'>, id:1747969808, size: 14
    variable: 72, type: <class 'int'>, id:1747969920, size: 14
    variable: 17, type: <class 'int'>, id:1747969040, size: 14
    variable: 66, type: <class 'int'>, id:1747969824, size: 14
    variable: 37, type: <class 'int'>, id:1747969360, size: 14
--------------------------------------------------
variable: 4, type: <class 'int'>, id:1747968832, size: 14
--------------------------------------------------
variable: [12, 100, 73, 64, 65, 72, 17, 66, 37], type: <class 'list'>, id:9924320, size: 76
    variable: 12, type: <class 'int'>, id:1747968960, size: 14
    variable: 100, type: <class 'int'>, id:1747970368, size: 14
    variable: 73, type: <class 'int'>, id:1747969936, size: 14
    variable: 64, type: <class 'int'>, id:1747969792, size: 14
    variable: 65, type: <class 'int'>, id:1747969808, size: 14
    variable: 72, type: <class 'int'>, id:1747969920, size: 14
    variable: 17, type: <class 'int'>, id:1747969040, size: 14
    variable: 66, type: <class 'int'>, id:1747969824, size: 14
    variable: 37, type: <class 'int'>, id:1747969360, size: 14
--------------------------------------------------
variable: 12, type: <class 'int'>, id:1747968960, size: 14
--------------------------------------------------
'''


def count_size(elements):
    for el in elements:
        print(f'variable: {el}, type: {type(el)}, id:{id(el)}, size: {size(el)}')
        try:
            len(el)
            for elc in el:
                print(f'    variable: {elc}, type: {type(elc)}, id:{id(elc)}, size: {size(elc)}')
        except TypeError:
            pass
        print('-' * 50)


count_size([series, least, series_copy, least_2])
