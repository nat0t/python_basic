'''Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        max_len = len(max((max(map(str, row), key=len) for row in self.matrix),
                          key=len))
        return '\n'.join([' '.join(f'{item:<{max_len}}' for item in row) for
                          row in self.matrix])

    def __add__(self, other):
        from copy import deepcopy
        result = deepcopy(self)
        result.matrix = [[(result.matrix[i][j] + other.matrix[i][j])
                          for j in range(len(self.matrix[i]))]
                          for i in range(len(self.matrix))]
        return result

matrix1 = Matrix([[400, 1, 5],
                    [6, 295, 23],
                    [31, 50000, 19]]
                   )
matrix2 = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
                 )
print('Output:')
print(matrix1)
print('Addition:')
print(matrix1 + matrix2)