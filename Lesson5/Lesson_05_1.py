'''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

file_obj = open('Lesson_05_1_file.txt', 'w+', encoding='utf-8')
while True:
    line = input('введите строку:')
    if line != '':
        print(f'{line}', file=file_obj)
        file_obj.write(line)
    else:
        break

file_obj.close()

# с контекстным менеджером
with open('Lesson_05_1_file.txt') as file_obj:
    while True:
        line = input('введите строку:')
        if line != '':
            print(f'{line}', file=file_obj)
            file_obj.write(line)
        else:
            break
