# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.


def average(value):
    mean = 0
    for el in value:
        mean += el['revenue']
    return mean / len(value)

def companies(value):
    mean = average(value)
    company_more = ''
    company_less = ''
    for el in value:
        if el['revenue'] > mean:
            company_more += el['name'] + '\n'
        elif el['revenue'] < mean:
            company_less += el['name'] + '\n'
    print(f'Средня прибыль предприятий составляет: {mean}\n'
          f'Компаний заработавщие выше среднего:\n{company_more}'
          f'Компаний заработавщие ниже среднего:\n{company_less}')


count = int(input('Введите колличество предприятий: '))
data = []
for _ in range(count):
    name = input('Введи название предприятия: ')
    revenue = float(input('Введите годовой доход предприятия: '))
    data.append({'name': name, 'revenue': revenue})
companies(data)
