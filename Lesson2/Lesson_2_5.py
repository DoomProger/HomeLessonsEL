'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]

while True:
    new_num = int(input('Введите число'))
    if my_list.count(new_num) == 0:
        if my_list[0] < new_num:
            my_list.insert(0, new_num)
        elif my_list[-1] > new_num:
            my_list.insert(len(my_list), new_num)
        else:
            for i in my_list[1:len(my_list)-1]:
                if new_num > i:
                    my_list.insert(my_list.index(i), new_num)
                    break

    elif my_list.index(new_num) >= 0:
        ind_x = my_list.index(new_num)
        count_num = my_list.count(new_num)
        my_list.insert(ind_x + count_num, new_num)

    cont = input('Продолжить? (y/n)')
    if cont == 'y':
        print(my_list)
        continue
    elif cont == '' or cont == 'n':
        break

print(my_list)

