'''Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class AltZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text

def divide(x: float, y: float) -> float:
    """
    Division of two numbers.
    :param x:
    :param y:
    :return:
    """
    if y == 0:
        raise AltZeroDivisionError('Division by zero!')
    return x / y

if __name__ == '__main__':
    x = input('Enter a dividend (x): ')
    y = input('Enter a divider (y): ')
    try:
        x, y = map(float, (x, y))
    except TypeError as error:
        print('Entered strings are not numbers.')

    try:
        print(f'x / y = {divide(x, y)}')
    except AltZeroDivisionError as error:
        print(error)