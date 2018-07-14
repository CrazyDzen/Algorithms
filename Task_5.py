# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter = input('Введите буквы, через запятую: ')
let = letter.split(', ')
letters = list(map(chr, range(ord('a'), ord('z')+1)))
i = letters.index(let[0]) + 1
j = letters.index(let[1]) + 1
if i > j:
    k = i - j - 1
else:
    k = j - i - 1

print(letters)
print(f'{let[0]} - {i} элемент алфавита'
      f'\n{let[1]} - {j} элемент алфавита'
      f'\nмежду ними {k} букв')


