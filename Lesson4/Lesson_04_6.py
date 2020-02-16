'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count

start = int(input('Стартовое число: '))
step = int(input('Шаг: '))

if step == '':
    step = 1


for el in count(start, step):
    if el > 15:
        break
    else:
        print(el)
