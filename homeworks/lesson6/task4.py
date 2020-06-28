'''Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go,
stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для
классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и также
покажите результат.
'''

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car has started.')

    def stop(self):
        print('The car has stopped.')

    def turn(self, direction):
        print(f'The car has turned {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}.')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('SPEED IS OVER!!!')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('SPEED IS OVER!!!')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

if __name__ == '__main__':
    print('Town car:')
    town_car = TownCar(65, 'black', 'Lexus')
    print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
    town_car.go()
    town_car.turn('left')
    town_car.show_speed()
    town_car.stop()
    print()

    print('Work car:')
    work_car = WorkCar(50, 'orange', 'Kamaz')
    print(work_car.speed, work_car.color, work_car.name, work_car.is_police)
    work_car.go()
    work_car.turn('right')
    work_car.show_speed()
    work_car.stop()
    print()

    print('Sport car:')
    sport_car = SportCar(50, 'red', 'Ferrari')
    print(sport_car.speed, sport_car.color, sport_car.name,
          sport_car.is_police)
    sport_car.go()
    sport_car.turn('right')
    sport_car.show_speed()
    sport_car.stop()
    print()

    print('Police car:')
    police_car = PoliceCar(90, 'blue', 'Ford')
    print(police_car.speed, police_car.color, police_car.name,
          police_car.is_police)
    police_car.go()
    police_car.turn('left')
    police_car.show_speed()
    police_car.stop()