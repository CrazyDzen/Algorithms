import random


# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.


def numbers():
    series = [random.randint(0, 100) for _ in range(1000000)]
    least = min(series)
    series_copy = series.copy()
    series_copy.remove(least)
    least_2 = min(series_copy)
    print(f'Два наименьших числа:{least}, {least_2}')


"""
100 loops, best of 3: 917 usec per loop - for range(100)
100 loops, best of 3: 5.42 msec per loop - for range(1000)
100 loops, best of 3: 47.2 msec per loop - for range(10000) 

for range(1000000)
         5268283 function calls in 6.557 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    6.557    6.557 <string>:1(<module>)
  1000000    2.281    0.000    4.650    0.000 random.py:173(randrange)
  1000000    0.997    0.000    5.647    0.000 random.py:217(randint)
  1000000    1.685    0.000    2.369    0.000 random.py:223(_randbelow)
        1    0.000    0.000    6.549    6.549 task_41.py:8(numbers)
        1    0.785    0.785    6.432    6.432 task_41.py:9(<listcomp>)
        1    0.000    0.000    6.557    6.557 {built-in method builtins.exec}
        2    0.109    0.054    0.109    0.054 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1000000    0.204    0.000    0.204    0.000 {method 'bit_length' of 'int' objects}
        1    0.006    0.006    0.006    0.006 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1268273    0.480    0.000    0.480    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.002    0.002    0.002    0.002 {method 'remove' of 'list' objects}

"""


def numbers_1():
    series = [random.randint(0, 100) for _ in range(1000000)]
    least = 100
    least_2 = 100
    for el in series:
        if el < least:
            least_2 = least
            least = el
        elif el == least:
            least_2 = el
        elif el < least_2:
            least_2 = el
    print(f'Два наименьших числа:{least}, {least_2}')


"""
100 loops, best of 3: 859 usec per loop
:0: UserWarning: The test results are likely unreliable. The worst
time (3.44e+03 usec) was more than four times slower than the best time. - for range(100)
100 loops, best of 3: 5.46 msec per loop - for range(1000)
100 loops, best of 3: 49.4 msec per loop - for range(10000) 

for range(1000000)
         5267396 function calls in 7.372 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    7.372    7.372 <string>:1(<module>)
  1000000    2.622    0.000    5.210    0.000 random.py:173(randrange)
  1000000    1.034    0.000    6.244    0.000 random.py:217(randint)
  1000000    1.844    0.000    2.589    0.000 random.py:223(_randbelow)
        1    0.278    0.278    7.368    7.368 task_41.py:46(numbers_1)
        1    0.846    0.846    7.090    7.090 task_41.py:47(<listcomp>)
        1    0.000    0.000    7.372    7.372 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1000000    0.210    0.000    0.210    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1267390    0.534    0.000    0.534    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


def amount():
    series = [random.randint(0, 100) for _ in range(1000000)]
    max_num = max(series)
    min_num = min(series)
    place_1 = series.index(max_num)
    place_2 = series.index(min_num)
    if place_1 > place_2:
        place_1, place_2 = place_2, place_1
    sum_series = sum(series[place_1 + 1: place_2])
    print(f'Сумма равна:{sum_series}')


"""
100 loops, best of 3: 848 usec per loop - for range(100)
100 loops, best of 3: 5.05 msec per loop - for range(1000)
100 loops, best of 3: 47.5 msec per loop - for range(10000) 

for range(1000000)
         5268013 function calls in 7.450 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    7.449    7.449 <string>:1(<module>)
  1000000    2.604    0.000    5.288    0.000 random.py:173(randrange)
  1000000    1.144    0.000    6.433    0.000 random.py:217(randint)
  1000000    1.900    0.000    2.684    0.000 random.py:223(_randbelow)
        1    0.000    0.000    7.445    7.445 task_41.py:92(amount)
        1    0.873    0.873    7.306    7.306 task_41.py:93(<listcomp>)
        1    0.000    0.000    7.450    7.450 {built-in method builtins.exec}
        1    0.072    0.072    0.072    0.072 {built-in method builtins.max}
        1    0.067    0.067    0.067    0.067 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
  1000000    0.228    0.000    0.228    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1268002    0.556    0.000    0.556    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""


def amount_2():
    series = [random.randint(0, 100) for _ in range(1000000)]
    least = 100
    least_id = 0
    most = -100
    most_id = 0
    for i in range(len(series)):
        if series[i] < least:
            least = series[i]
            least_id = i
        if series[i] > most:
            most = series[i]
            most_id = i
    if least_id > most_id:
        least_id, most_id = most_id, least_id
    sum_series = 0
    for i in range(least_id + 1, most_id):
        sum_series += series[i]
    print(f'Сумма равна:{sum_series}')


"""
100 loops, best of 3: 871 usec per loop - for range(100)
100 loops, best of 3: 5.49 msec per loop - for range(1000)
100 loops, best of 3: 49.5 msec per loop - for range(10000) 

for range(1000000)
         5266943 function calls in 7.747 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    7.747    7.747 <string>:1(<module>)
  1000000    2.502    0.000    5.291    0.000 random.py:173(randrange)
  1000000    1.032    0.000    6.323    0.000 random.py:217(randint)
  1000000    2.007    0.000    2.789    0.000 random.py:223(_randbelow)
        1    0.387    0.387    7.745    7.745 task_41.py:133(amount_2)
        1    1.035    1.035    7.357    7.357 task_41.py:134(<listcomp>)
        1    0.000    0.000    7.747    7.747 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1000000    0.212    0.000    0.212    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1266936    0.569    0.000    0.569    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


def replacement():
    series = [random.randint(0, 100) for _ in range(1000000)]
    most = max(series)
    least = min(series)
    most_id = series.index(most)
    least_id = series.index(least)
    series.insert(least_id, most)
    series.pop(least_id + 1)
    series.insert(most_id, least)
    series.pop(most_id + 1)


"""
100 loops, best of 3: 469 usec per loop - for range(100)
100 loops, best of 3: 4.56 msec per loop - for range(1000)
100 loops, best of 3: 45.4 msec per loop - for range(10000) 

for range(1000000)
         5267395 function calls in 6.836 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    6.836    6.836 <string>:1(<module>)
  1000000    2.407    0.000    4.900    0.000 random.py:173(randrange)
  1000000    1.032    0.000    5.932    0.000 random.py:217(randint)
  1000000    1.790    0.000    2.493    0.000 random.py:223(_randbelow)
        1    0.000    0.000    6.833    6.833 task_41.py:183(replacement)
        1    0.783    0.783    6.715    6.715 task_41.py:184(<listcomp>)
        1    0.000    0.000    6.836    6.836 {built-in method builtins.exec}
        1    0.057    0.057    0.057    0.057 {built-in method builtins.max}
        1    0.054    0.054    0.054    0.054 {built-in method builtins.min}
  1000000    0.205    0.000    0.205    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1267382    0.498    0.000    0.498    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        2    0.004    0.002    0.004    0.002 {method 'insert' of 'list' objects}
        2    0.004    0.002    0.004    0.002 {method 'pop' of 'list' objects}
"""


def replacement_2():
    series = [random.randint(0, 100) for _ in range(1000000)]
    most = -100
    most_id = 0
    least = 100
    least_id = 0
    for i in range(len(series)):
        if series[i] < least:
            least = series[i]
            least_id = i
        if series[i] > most:
            most = series[i]
            most_id = i
    series.insert(least_id, most)
    series.pop(least_id + 1)
    series.insert(most_id, least)
    series.pop(most_id + 1)


"""
100 loops, best of 3: 470 usec per loop - for range(100)
100 loops, best of 3: 4.79 msec per loop - for range(1000)
100 loops, best of 3: 47.3 msec per loop - for range(10000) 

for range(1000000)
         5267768 function calls in 6.832 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    6.831    6.831 <string>:1(<module>)
  1000000    2.269    0.000    4.702    0.000 random.py:173(randrange)
  1000000    0.938    0.000    5.640    0.000 random.py:217(randint)
  1000000    1.744    0.000    2.433    0.000 random.py:223(_randbelow)
        1    0.373    0.373    6.828    6.828 task_41.py:224(replacement_2)
        1    0.806    0.806    6.447    6.447 task_41.py:225(<listcomp>)
        1    0.000    0.000    6.832    6.832 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
  1000000    0.201    0.000    0.201    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1267758    0.488    0.000    0.488    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.004    0.002    0.004    0.002 {method 'insert' of 'list' objects}
        2    0.004    0.002    0.004    0.002 {method 'pop' of 'list' objects}
"""
