'''Реализовать программу работы с органическими клетками. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству клеток (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение
(__add__()), вычитание (__sub__()), умножение (__mul__()), деление
(__truediv__()).Данные методы должны применяться только к клеткам и
выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки
должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
если разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки
определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух
клеток.
В классе необходимо реализовать метод make_order(), принимающий
экземпляр класса и количество ячеек в ряду. Данный метод позволяет
организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где
количество ячеек между \n равно переданному аргументу. Если ячеек на
формирование ряда не хватает, то в последний ряд записываются все
оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в
ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''
class CellException(Exception):
    def __init__(self, text):
        self.text = text

class Cell:
    def __init__(self, number):
        if number > 0:
            self.number = number
        else:
            raise CellException('Number of cells must be positive.')

    def __add__(self, other):
        result = Cell(1)
        result.number = self.number + other.number
        return result

    def __sub__(self, other):
        if self.number > other.number:
            result = Cell(1)
            result.number = self.number - other.number
            return result
        raise CellException('Number of cells must be positive.')

    def __mul__(self, other):
        result = Cell(1)
        result.number = self.number * other.number
        return result

    def __truediv__(self, other):
        result = Cell(1)
        result.number = round(self.number / other.number)
        if result.number > 0:
            return result
        raise CellException('Number of cells must be positive.')

    def make_order(self, cells_in_row):
        rows, residue = divmod(self.number, cells_in_row)
        return ('*' * cells_in_row + '\n') * rows + '*' * residue

if __name__ == '__main__':
    cell1 = Cell(14)
    cell2 = Cell(20)

    print((cell1 + cell2).number)

    try:
        print((cell1 - cell2).number)
    except CellException as error:
        print(error)

    print((cell1 * cell2).number)

    try:
        print((cell1 / cell2).number)
    except CellException as error:
        print(error)

    print(cell1.make_order(4))
    print(cell2.make_order(8))