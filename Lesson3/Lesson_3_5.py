'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def find_q(val):
    for index, v in enumerate(val):
        if v == 'q':
            if val.count('q') >= 0:
                return index
        else:
            continue
            # print('no q')


def sum_val(arg, ind):
   sums = 0

    if ind == None:
        b = map(int, arg)
        sums = sum(b)
        return sums
    else:
        arg.pop(ind)
        b = list(map(int, arg))
        sums = sum(b)
        return sums

while True:
    #e = '1 2 3 q'
    e = input('Введите числа разделенные пробелами: ')
    e = list(e.split())
    print('сумма', sum_val(e, find_q(e)))


    if find_q(e) == 0:
        print('wxit')
        break
