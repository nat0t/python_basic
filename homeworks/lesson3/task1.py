'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''
def my_division(x, y) -> float:
    """
    My implementation of dividing two numbers.
    :param x:
    :param y:
    :return:
    """
    try:
        return float(x) / float(y)
    except ValueError:
        print("It's not numbers.")
    except ZeroDivisionError:
        print('Cannot be divided by zero.')
    else:
        print('Unknown error.')

x = input('Enter dividend (x): ')
y = input('Enter divider (y): ')
print(f'x / y = {my_division(x, y)}')