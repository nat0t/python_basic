'''Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может
иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для
пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить
работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора
@property.
'''

import abc

class Cloth(abc.ABC):
    __total = []

    def __init__(self, size):
        self.size = size
        Cloth.__total.append(self)

    @abc.abstractmethod
    def get_square(self):
        pass

    @staticmethod
    def total_square():
        result = 0
        for item in Cloth.__total:
            result += item.get_square
        return result

class Coat(Cloth):
    @property
    def get_square(self):
        return self.size / 6.5 + 0.5

class Suit(Cloth):
    @property
    def get_square(self):
        return 2 * self.size + 0.3

if __name__ == '__main__':
    coat1 = Coat(2)
    print(coat1.get_square)
    coat2 = Coat(5)
    print(coat2.get_square)
    suit1 = Suit(3)
    print(suit1.get_square)
    suit2 = Suit(4)
    print(suit2.get_square)
    print(Cloth.total_square())