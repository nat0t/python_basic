'''Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

def fact(n: int) -> int:
    """
    Function takes parameter 'n' and returns 'n!'.
    :param n:
    :return:
    """
    import math
    number = 1
    if n == 0:
        yield 0, 1
    else:
        while number <= n:
            yield number, math.factorial(number)
            number += 1

while True:
    try:
        n = int(input('Enter natural number: '))
        break
    except ValueError:
        print('Enter natural number!')

for number, fact_ in fact(n):
    print(f'{number}! = {fact_}')