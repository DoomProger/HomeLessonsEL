'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''


import re
from functools import reduce
my_dict = {}


def sum_int_el(el1, next_el1):
    return int(el1) + int(next_el1)


with open('lesson_05_6_acsub.txt', encoding='utf-8') as file_as:
    for x in file_as:
        my_dict.setdefault(list(x.split(':'))[0], list((x.split(':')))[1])

print(my_dict)

for key, val in my_dict.items():
    my_dict.update({key: reduce(sum_int_el, re.findall(r'\d+', val))})

print(my_dict)
