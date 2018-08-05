# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import randint


def sort(l, r):
    merge = []
    while l and r:
        if l[0] > r[0]:
            merge.append(r.pop(0))
        else:
            merge.append(l.pop(0))
    if l:
        merge.extend(l)
    if r:
        merge.extend(r)
    return merge


def merge_sort(li):
    if len(li) < 2:
        return li
    mid = int(len(li) / 2)
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    return sort(left, right)


my_list = [randint(-100, 99) for _ in range(10)]
print(my_list)
print(merge_sort(my_list))
