'''Создать текстовый файл (не программно), сохранить в нем несколько
строк, выполнить подсчет количества строк, количества слов в каждой
строке.
'''

with open('hamlet.txt') as file:
    lines = file.readlines()
print(f'Number of lines in file {file.name}: {len(lines)}')
for index, line in enumerate(lines, 1):
    print(f'Number of words in line {index}: {len(line.split())}')