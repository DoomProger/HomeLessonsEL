'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''

import random

new_list = [el*random.randrange(-11, 11) for el in range(20)]
print(new_list)

for i, v in enumerate(new_list):
    if new_list.count(v) > 1:
        srez = new_list.index(v) + 1
        indx_list = new_list[srez:].index(v) + srez
        new_list.pop(indx_list)

print()
print(new_list)
