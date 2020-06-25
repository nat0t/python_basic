'''Создать (программно) текстовый файл, записать в него программно набор
чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
в файле и выводить ее на экран.
'''

numbers = [item for item in range(50) if item % 4 == 1]
with open('numbers.txt', 'w') as file:
    for number in numbers:
        print(number, end=' ', file=file)

with open('numbers.txt') as file:
    print(f'Sum of numbers: {sum(map(float, (file.readlines()[0].split())))}')