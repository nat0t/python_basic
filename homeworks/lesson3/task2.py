'''Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
def person(name: str, surname: str, year: str,
           address: str, email: str, phone: str) -> str:
    """
    Function returns information about person in one line.
    :param name:
    :param surname:
    :param year:
    :param address:
    :param email:
    :param phone:
    :return:
    """
    return (f"Name: {name} {surname}, year of birth: {year}, address: {address}, "
                     f"e-mail: {email}, phone: {phone}.")

if __name__ == '__main__':
    name = input('Enter name of person: ')
    surname = input('Enter surname of person: ')
    year = input('Enter year of person: ')
    address = input('Enter address of person: ')
    email = input('Enter e-mail of person: ')
    phone = input('Enter phone of person: ')
    print(person(name=name, surname=surname, year=year, address=address,
                 email=email, phone=phone))