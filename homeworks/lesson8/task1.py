'''Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках класса
реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу
полученной структуры на реальных данных.
'''

class Date:
    @classmethod
    def _extract_date(cls, date: str) -> tuple:
        """
        Extracting date.
        :param date:
        :return:
        """
        if cls.__check2(date):
            return tuple((map(int, date.split('-'))))
        print(f'"Date" {date} is not valid.')

    @staticmethod
    def __check1(date: str) -> bool:
        """
        Validating date (only for years from 1000 to 9999).
        :param date:
        :return:
        """
        from time import strptime
        try:
            strptime(date, '%d-%m-%Y')
            return True
        except ValueError as error:
            return False

    @staticmethod
    def __check2(date: str) -> bool:
        """
        Validating date.
        :param date:
        :return:
        """
        try:
            d, m, y = tuple((map(int, date.split('-'))))
        except ValueError as error:
            return False
        # Checking leap year.
        leap_year = False if y % 4 or not y % 100 and y % 400 else True
        # Checking month.
        if 1 <= m <= 12:
            last_day = 30 if m in (4, 6, 9, 11) else 31
            last_day = 29 if leap_year and m == 2 else 28
        # Checking day.
        return True if 1 <= d <= last_day else False
        return False

if __name__ == '__main__':
    date1 = '29-02-1600'
    date2 = 'a2-12-1'
    date3 = '41-01-1985'
    print(Date._extract_date(date1))
    print(Date._extract_date(date2))
    print(Date._extract_date(date3))