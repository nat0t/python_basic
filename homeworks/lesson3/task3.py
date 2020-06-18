'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
def my_func(x, y, z):
    """
    Function returns the sum of the two largest arguments.
    :param x:
    :param y:
    :param z:
    :return:
    """
    try:
        return sum(sorted((float(x), float(y), float(z))[:2], reverse=True))
    except ValueError:
        print("It's not numbers.")

if __name__ == '__main__':
    print(my_func(15, -4.2, -21.7))