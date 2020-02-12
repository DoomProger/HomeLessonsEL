'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


# Вариант 1
def human(name, surname, date_birth, city, email, mob):
    return print(f'Имя:{name} Фамилия:{surname} Дата рождения:{date_birth} '
                 f'Город:{city} Электронная почта:{email} '
                 f'Мобильный телефон:{mob}')
human(
    name=input('имя: '),
    surname=input('фамилия: '),
    date_birth=input('дата рождения: '),
    city=input('город: '),
    email=input('email: '),
    mob=input('мобильный: ')
    )


# Вариант 2
print('Вариант 2, данные пользователя в словаре')
def human_se(name, surname, date_birth, city, email, mob):
    return print(f'Имя:{name} Фамилия:{surname} Дата рождения:{date_birth} '
                 f'Город:{city} Электронная почта:{email} '
                 f'Мобильный телефон:{mob}')


human_list = {'имя': '', 'фамилия': '', 'дата рождения': '', 'город': '', 'email': '', 'мобильный': ''}
for f in human_list.keys():
    user_data = input('{}: '.format(f))
    human_list[f] = user_data

human_se(
    name=human_list.setdefault('имя'),
    surname=human_list.setdefault('фамилия'),
    date_birth=human_list.setdefault('дата рождения'),
    city=human_list.setdefault('город'),
    email=human_list.setdefault('email'),
    mob=human_list.setdefault('мобильный')
    )


