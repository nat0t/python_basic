'''Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую
структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества
принтеров, отправленных на склад, нельзя использовать строковый тип
данных.
'''

class OfficeError(Exception):
    def __init__(self, text):
        self.text = text

class OfficeEquipment:
    def __init__(self, model: str, price: int):
        self.model = model
        try:
            self.price = price
        except ValueError as error:
            print('Incorrect price of equipment. Set to zero.')
            self.price = 0

class Printer(OfficeEquipment):
    def __init__(self, model, price, is_color: bool):
        super().__init__(model, price)
        self.type = 'printer'
        self.is_color = is_color

    def print(self, document):
        if not isinstance(document, Document):
            print("I can't print it.")
        else:
            print(f'Printing "{document.name}" in progress... ')

class Scanner(OfficeEquipment):
    def __init__(self, model, price, dpi: int):
        super().__init__(model, price)
        self.type = 'scanner'
        self.dpi = dpi

    def scan(self, document):
        if not isinstance(document, Document):
            print("I can't scan it.")
        else:
            print(f'Scanning "{document.name}" in progress..."')

class Copier(OfficeEquipment):
    def __init__(self, model, price, speed: int):
        super().__init__(model, price)
        self.type = 'copier'
        self.speed = speed

    def copy(self, document):
        if not isinstance(document, Document):
            print("I can't copy it.")
        else:
            print(f'Copying "{document.name}" in progress...')

class Document:
    def __init__(self, name: str, content: str = ''):
        self.name = name
        self.content = content

class Storage:
    def __init__(self, name: str):
        self.__name = name
        self.__content = {}

    @property
    def name(self):
        return self.__name

    @property
    def content(self):
        print(f'Content of {self.name}:')
        result = [f'{item.model}: {self.__content[item]}' for item in \
                  self.__content]
        return result

    def add(self, item, quantity):
        if not isinstance(quantity, int):
            print('Incorrect quantity for adding.')
        elif isinstance(item, OfficeEquipment):
            self.__content[item] = (self.__content[item] + int(quantity)) if item in \
                self.__content.keys() else int(quantity)
            print(f'Added {quantity} {item.model} to {self.name}.')
        else:
            print('Incorrect item for adding.')

    def give(self, item, quantity, destination):
        if not isinstance(quantity, int):
            print('Incorrect quantity for giving.')
        elif not isinstance(item, OfficeEquipment):
            print('Incorrect item for giving.')
        elif not isinstance(destination, Storage):
            print('Incorrect destination place for giving.')
        else:
            quantity = int(quantity)
            if self.__content[item] >= quantity:
                self.__content[item] -= quantity
                destination.add(item, quantity)
                print(f'Removed {quantity} {item.model} from {self.__name}')
            else:
                print(f'Not enough {item.model} for transfer in {self.__name}.'
                      f' Transfer is not completed.')

if __name__ == '__main__':
    document = Document('Annual report', 'This year we all did a great job...')
    head_store = Storage('main_store')
    branch_store = Storage('branch_store')
    printer = Printer('HP LaserJet Pro P1102', 17600, False)
    scanner = Scanner('HP ScanJet Pro 2500 f1', 22640, 360000)
    copier = Copier('Duplo DP-F550', 783500, 150)

    printer.print(document)
    scanner.scan(document)
    copier.copy(document)
    print()

    head_store.add(printer, 10)
    head_store.add(scanner, 5)
    head_store.add(copier, 2)
    print()
    print(head_store.content)
    print(branch_store.content)
    print()

    head_store.give(printer, 5, branch_store)
    head_store.give(scanner, 5, branch_store)
    head_store.give(copier, 5, branch_store)
    print()
    print(head_store.content)
    print(branch_store.content)