from random import randint

'''
Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными 
числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
'''


def bubble_sort(li):
    for i in range(1, len(li)):
        n = 0
        for j in range(0, len(li) - i):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                n += 1
        if n == 0:
            break
    return li


my_list = [randint(-100, 99) for _ in range(10)]
print(my_list)
print(bubble_sort(my_list))
