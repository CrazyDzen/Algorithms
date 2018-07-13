# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number = int(input('Введите цифру от 1 до 26: '))
letters = list(map(chr, range(ord('a'), ord('z')+1)))
a = letters[number - 1]
print(f'Это буква {a}')


