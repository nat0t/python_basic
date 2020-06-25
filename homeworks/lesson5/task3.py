'''Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
'''

with open('salary.txt') as file:
    staff = file.readlines()
average = 0
print('Underpaid staff:')
for employee in staff:
    employee = employee.split()
    average += float(employee[2])
    if float(employee[2]) < 20000:
        print(employee[1])
print(f'Average salary of all staff: {average / len(staff)}')