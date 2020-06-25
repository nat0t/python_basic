'''Создать программно файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
свидетельствует пустая строка.
'''

text = None
while text != '':
    text = input('Enter a line of text (empty line for stop):\n')
    with open('text.txt', 'a') as file:
        file.write(text + '\n')