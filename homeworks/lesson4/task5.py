'''Реализовать формирование списка, используя функцию range() и
возможности генератора. В список должны войти четные числа от 100
до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

import functools
result = [item for item in range(100, 1001) if not item & 1]
print(result)
composition = functools.reduce(lambda x1, x2: x1 * x2, result)
print(composition)