'''Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого для
покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу
метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road():
    _mass = 25
    _depth = 5

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def mass_calc(self):
        return self._length * self._width * Road._mass * Road._depth

if __name__ == '__main__':
    while True:
        try:
            length = float(input('Enter length of the road in meters: '))
            width = float(input('Enter width of the road in meters: '))
        except ValueError:
            print('Incorrect input.')
            continue
        if length < 0 or width <= 0:
            print('Entered negative number(-s).')
            continue
        break
    road = Road(length, width)
    print(f'Asphalt mass for road {length}m * {width}m * {road._mass}kg '
            f'* {road._depth}cm is {road.mass_calc()}kg.')