# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

numbers = []
while True:
    k = int(input('Введите натуральное число, есливы хотите остановиться введите "0": '))
    if k == 0:
        break
    numbers.append(k)
most = 0
amount = 0
for el in numbers:
    n = []
    k = el
    while k != 0:
        n.append(k % 10)
        k = k // 10
    if sum(n) > most:
        most = el
        amount = sum(n)

print(f'Наибольшая сумма цифр у числа: {most}, '
      f'\nСумма его чисел равна: {amount}')