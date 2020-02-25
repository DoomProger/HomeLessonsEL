'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv

script_name, work_hour, rph = argv

work_hour = int(work_hour)
rph = float(rph)


def wages():
    result = (work_hour * rph) + (work_hour * rph) * 0.3
    print(f'Премия 30% от ЗП: {(float((work_hour * rph) * 0.3)):.2f}')
    return print(f'Итого ЗП: {result}')


wages()

'''
C:\Repos\HomeLessonsEL\Lesson4>python Lesson_04_1.py 8 230.2
Премия 30% от ЗП: 552.48
Итого ЗП: 2394.08
'''