'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
'''

with open('count_en.txt') as file:
    lines = file.readlines()

count = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
lines_ru = [line.replace(key, item) for line in lines for key, item in \
            count.items() if key in line]

with open('count_ru.txt', 'w', encoding='UTF-8') as file:
    file.writelines(lines_ru)