'''Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом: for
el in fact(n). Функция отвечает за получение факториала числа, а
в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

def fact1(n: int) -> int:
    """
    Function takes parameter 'n' and returns 'n!'.
    :param n:
    :return:
    """
    import math
    number = 1
    while number <= n:
        yield number, math.factorial(number)
        number += 1

def fact2(n: int) -> int:
    """
    Function takes parameter 'n' and returns 'n!'.
    :param n:
    :return:
    """
    start = 1
    result = 1
    while n >= start:
        yield result
        start += 1
        result *= start

while True:
    try:
        n = int(input('Enter natural number: '))
        break
    except ValueError:
        print('Enter natural number!')

print('Variant 1:')
for number, fact_ in fact1(n):
    print(f'{number}! = {fact_}')
print('Variant 2:')
for index, number in enumerate(fact2(n), 1):
    print(f'{index}! = {number}')