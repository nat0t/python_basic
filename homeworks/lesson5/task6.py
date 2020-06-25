'''Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и
лабораторных занятий по этому предмету и их количество. Важно, чтобы для
каждого предмета не обязательно были все типы занятий. Сформировать
словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

with open('syllabus.txt', 'r', encoding='UTF-8') as file:
    subjects = file.readlines()

subjects = map(lambda s: s.replace('(л)', ''), subjects)
subjects = map(lambda s: s.replace('(пр)', ''), subjects)
subjects = map(lambda s: s.replace('(лаб)', ''), subjects)
subjects = map(lambda s: s.replace('-', ''), subjects)

lessons = {subject.split()[0]: sum(map(int, subject.split()[1:])) for subject \
           in subjects}
print(lessons)