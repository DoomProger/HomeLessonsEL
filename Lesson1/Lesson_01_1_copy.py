'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран.
'''

a = 10
b = a + 5
print("10+5 =", b)

c = '11'
d = 12
b = 5
e = int(c) + 12
print(e, b + d)

# ---------
print('--------------')

us = 62
eu = 71.2

rub = int(input('Сколько рублей вы ходите конвертировать в US и EU:'))

usconversion = round(rub/us, 2)
euconversion = round(rub/eu, 2)

print(usconversion, 'US')
print(euconversion, 'EU')

#--------
name = input('Как вас звать?:')
age = int(input('Сколько вам лет?:'))
print('Через 10 лет', name, 'будет', age + 10)
