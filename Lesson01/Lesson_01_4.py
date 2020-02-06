'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

num = int(input('Введите целое положительное число: '))
while True:
    if num > 0:
        result = -1
        break
    elif num == 0:
        result = num
        break
    else:
        print('Чило не положительное')
        num = int(input('Введите целое положительное число'))

while num > 10:
    ost_del = num % 10
    num //= 10
    if ost_del > result:
        result = ost_del
print('Cамая большая цифра: ', result)
