'''Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись без
встроенной функции возведения числа в степень.'''
def my_func1(x: float, y: int) -> float:
    """
    Function raises 'x' to a power 'y'. 'x' - float positive, 'y' - integer negative.
    :param x:
    :param y:
    :return:
    """
    try:
        return float(x) ** int(y) if float(x) > 0 and int(y) < 0 else print("Wrong numbers.")
    except ValueError:
        print("It's not number.")
    else:
        print('Unknown error.')

def my_func2(x: float, y: int) -> float:
    """
        Function raises 'x' to a power 'y'. 'x' - float positive, 'y' - integer negative.
        :param x:
        :param y:
        :return:
        """
    result = 1
    try:
        x = float(x)
        y = int(y)
        if x > 0 and y < 0:
            while y < 0:
                result *= 1 / x
                y += 1
            return result
        else:
            print('Wrong numbers.')
    except ValueError:
        print("It's not number.")
    else:
        print('Unknown error.')

def my_func3(x: float, y: int) -> float:
    """
        Function raises 'x' to a power 'y'. 'x' - float positive, 'y' - integer negative or zero.
        :param x:
        :param y:
        :return:
        """
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y > 0:
            print('Wrong numbers.')
            return
        if y == 0:
            return 1
        else:
            return (1/x) * my_func3(x, y+1)
    except ValueError:
        print("It's not number.")
    else:
        print('Unknown error.')