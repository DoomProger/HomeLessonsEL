'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
        return result
    except ZeroDivisionError:
        result = 'Деление на ноль!'
        return result

arg_1 = float(input('Введите 1-ю цифру: '))
arg_2 = float(input('Введите 2-ю цифру: '))
print('Результат деления: ', division(arg_1, arg_2))
