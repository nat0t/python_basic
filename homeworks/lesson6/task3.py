'''Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход). Последний
атрибут должен быть защищенным и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе
Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income). Проверить
работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
'''

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

if __name__ == '__main__':
    person1 = Position('Joe', 'Smith', 'manager', 1000, 500)
    print(person1.name)
    print(person1.surname)
    print(person1.position)
    print(person1._income)
    print(person1.get_full_name())
    print(person1.get_total_income())

    person2 = Position('Ann', 'Black', 'programmer', 2000, 1000)
    print(person2.name)
    print(person2.surname)
    print(person2.position)
    print(person2._income)
    print(person2.get_full_name())
    print(person2.get_total_income())