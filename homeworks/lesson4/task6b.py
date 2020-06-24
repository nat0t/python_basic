'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного
заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при
достижении числа 10 завершаем цикл. Во втором также необходимо
предусмотреть условие, при котором повторение элементов списка будет
прекращено.
'''

import itertools
source = [item for item in range(1, 5)]
print(source)

while True:
    try:
        repeat = int(input('Enter number of reiterations: '))
        break
    except ValueError:
        print('Enter natural number!')

for index, item in enumerate(itertools.cycle(source), 1):
    if index > repeat:
        break
    else:
        print(item, end=' ')