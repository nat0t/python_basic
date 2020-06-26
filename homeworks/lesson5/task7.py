'''Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
{"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''

import json

with open('company.txt') as file:
    data = file.readlines()

average = 0
company = []
count = 0
for firm in data:
    firm = firm.split()
    revenue, costs = map(int, firm[2:])
    profit = revenue - costs
    company.append({firm[0]: profit})
    if profit >= 0:
        average += profit
        count += 1
average = average / count
company.append({'average_profit': average})

with open('company_json.txt', 'w') as file:
    json.dump(company, file)