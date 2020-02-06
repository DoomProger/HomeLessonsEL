'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
'''

num = int(input('Введите число:'))

num = str(num)
twonum = num + num
threenum = num + num + num

sum = int(num)+int(twonum)+int(threenum)
print(f"Считаем {num} + {twonum} + {threenum} = {sum}")

