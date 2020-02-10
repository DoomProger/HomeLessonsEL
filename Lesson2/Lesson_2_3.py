'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
'''

times_year = {1: 'Зима', 2: 'Зима', 3: 'Зима',
              4: 'Весна', 5: 'Весна', 6: 'Весна',
              7: 'Лето', 8: 'Лето', 9: 'Лето',
              10: 'Осень', 11: 'Осень', 12: 'Осень'}

while True:
    try:
        mounth_num = int(input('Введите номер месяца (от 1 до 12):'))
        print(f'Этот месяц совпадает со временем года {times_year.get(mounth_num)}')
        break
    except ValueError:
        print('Вы ввели не номер масяца, попробуйте еще раз')


print('Тоже самое только списком')
print('-------------------------')

times_year_list = ['зима', 'весна', 'лето', 'осень']

while True:
    try:
        mounth_num_list = int(input('Введите номер месяца (от 1 до 12):'))
        if 3 >= mounth_num_list >= 1:
            print(f'Время года {times_year_list[0]}')
        elif 6 >= mounth_num_list >= 4:
            print(f'Время года {times_year_list[1]}')
        elif 9 >= mounth_num_list >= 7:
            print(f'Время года {times_year_list[2]}')
        elif 12 >= mounth_num_list >= 7:
            print(f'Время года {times_year_list[3]}')
        break
    except ValueError:
        print('Вы ввели не номер масяца, попробуйте еще раз')
