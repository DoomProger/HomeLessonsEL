'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


from functools import reduce

def list_to_str(list_in):
    str_in = ' '
    return str_in.join(list_in)


def sum_int_el(el1, next_el1):
    return int(el1) + int(next_el1)


with open('lesson_05_5_num.txt', 'w+', encoding='utf-8') as file_obj:
    my_list = [str(x) for x in range(1, 11)]
    print(f'Последовательность записываемая в файл: {list_to_str(my_list)}')
    file_obj.write(list_to_str(my_list))

with open('lesson_05_5_num.txt', encoding='utf-8') as r_file:
    xx = (r_file.read().split(' '))
    result = reduce(sum_int_el, xx)
    print(f'Сумма последовательности чисел: {result}')
