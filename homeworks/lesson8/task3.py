'''Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу исключения
на реальном примере. Необходимо запрашивать у пользователя данные и
заполнять список. Класс-исключение должен контролировать типы данных
элементов списка.
'''

class NotOnlyNumbersError(Exception):
    def __init__(self, text):
        self.text = text

if __name__ == '__main__':
    list_ = []
    while True:
        try:
            try:
                item = input('Enter a number for append to list (to stop '
                             'typing enter nothing and press "Enter"): ')
                if item == '':
                    break
                list_.append(float(item))
                print(f'Updated list: {list_}')
            except ValueError as error:
                raise NotOnlyNumbersError('Entered item is not a number.')
        except NotOnlyNumbersError as error:
            print(error)
    print(f'Summary list: {list_}')