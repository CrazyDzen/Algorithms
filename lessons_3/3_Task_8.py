# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
# последнюю ячейку строки. В конце следует вывести полученную матрицу


matrix = []
for i in range(4):
    enter = input(f'Введите 4 элемента {i+1} строки, через запятую: ')
    list_str = enter.split(',')
    list_int = [int(el) for el in list_str]
    list_int.append(sum(list_int))
    matrix.append(list_int)
for i in range(4):
    print(matrix[i])
