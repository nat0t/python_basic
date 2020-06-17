'''Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
def person(name: str, surname: str, year: str,
           address: str, email: str, phone: str) -> str:
    """Function returns information about person in one line.
    """
    person_info = {}
    person_info['name'] = name
    person_info['surname'] = surname
    person_info['year'] = year
    person_info['address'] = address
    person_info['email'] = email
    person_info['phone'] = phone
    return (f"Name: {person_info['name']} {person_info['surname']}, "
            f"year of birth: {person_info['year']}, address: {person_info['address']}, "
            f"e-mail: {person_info['email']}, phone: {person_info['phone']}.")

name = input('Enter name of person: ')
surname = input('Enter surname of person: ')
year = input('Enter year of person: ')
address = input('Enter address of person: ')
email = input('Enter e-mail of person: ')
phone = input('Enter phone of person: ')
print(person(name=name, surname=surname, year=year, address=address,
             email=email, phone=phone))