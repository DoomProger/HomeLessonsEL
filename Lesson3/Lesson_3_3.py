'''
Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''


def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    min_arg = min(my_list)
    return sum(my_list) - min_arg


arg = []
for el in range(0, 3):
    arg.append(float(input('Введите число:')))

print(f'Сумма наибольших двух аргументов из {arg} это {my_func(arg[0], arg[1], arg[2])}')


