'''
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
'''

import random

new_list = [el*random.randrange(-11, 11) for el in range(10)]
print(new_list)
k = []
for i, ell in enumerate(new_list):
    if i == 0:
        continue
    else:
        k.append(new_list[i]) if new_list[i] > new_list[i-1] else None

print(k)
