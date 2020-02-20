'''
Создать текстовый файл (не программно),сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open('lesson_05_2_filecount.txt') as file_obj:
    print(f'Количество строк в файле: {len(file_obj.readlines())}')
    file_obj.seek(0)
    print(f'Количество символов в файле : {len(file_obj.read())}')
    file_obj.seek(0)

    i = 1

    for line in file_obj:
        print(f'Количество слов в строке: {i} - {len(list(line.split()))}')
        i += 1
