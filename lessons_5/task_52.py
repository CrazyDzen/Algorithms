# Используя конспект, написать программу сложения и умножения двух шестнадцатеричных
# чисел. При этом каждое число представляется как массив, элементы которого – это цифры числа.


num_let = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
let_num = {v: k for k, v in num_let.items()}


def ten(line_one):
    line = line_one.lower()
    number = []
    for el in line[::-1]:
        el.upper()
        try:
            number.append(num_let[el])
        except KeyError:
            print('Введеное число не является шестнадцатиричным попробуй еще раз!')
            main()
    return number


def sixteen(number):
    line = ''
    for el in number[::-1]:
        line += str(let_num[el])
    return line


def amount(a, b):
    if len(a) < len(b):
        a, b = b, a
    reg = 0
    sum_numbers = []
    for i in range(len(a)):
        if len(b) > i:
            c = a[i] + b[i] + reg
        else:
            c = a[i] + reg
        reg = 0
        if c > 15:
            reg = 1
            c = c - 16
        sum_numbers.append(c)
    return sum_numbers


def multiplication(a, b):
    if len(a) < len(b):
        a, b = b, a
    previous = []
    for i in range(len(b)):
        reg = 0
        numbers = []
        for _ in range(i):
            numbers.append(0)
        for j in range(len(a)):
            c = a[j] * b[i] + reg
            reg = 0
            if c > 15:
                reg = c // 16
                c = c % 16
            numbers.append(c)
            if j == len(a) - 1:
                numbers.append(reg)
        previous = amount(previous, numbers)
    return previous


def main():
    num_one = input('Введите первое число: ')
    one = ten(num_one)
    num_two = input('Введите второе число: ')
    two = ten(num_two)
    print(f'Сумма чисел: {sixteen(amount(one, two))},'
          f'\nПроизведение: {sixteen(multiplication(one, two))}')


main()
