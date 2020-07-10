'''Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
'''

class Complex:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 1:
            return (f'{self.a}+i')
        elif self.b == -1:
            return (f'{self.a}-i')
        if self.b > 0:
            return (f'{self.a}+{self.b}i')
        elif self.b < 0:
            return (f'{self.a}{self.b}i')
        else:
            return (f'{self.a}')

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b )
        else:
            print('Can be sum only complex numbers.')

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a*other.a - self.b*other.b,
                           self.a*other.b + self.b*other.a)
        else:
            print('Can be multiply only complex numbers.')

if __name__ == '__main__':
    x = Complex(1, 2)
    y = Complex(5, -3)
    z = Complex(2, 0)

    print(x)
    print(y)
    print(z)

    print(f'x + y = {x + y}')
    print(f'(x + y) * z = {(x + y) * z}')