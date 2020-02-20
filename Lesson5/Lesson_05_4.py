'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

ru_name = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

def list_to_str(list_in):
    str_in = ' '
    return str_in.join(list_in)


with open('lesson_05_4_num.txt', encoding='utf-8') as file_obj:
    s = [i.split() for i in file_obj]
    with open('lesson_05_4_num_ru.txt', 'w', encoding='utf-8') as file1_obj:
        for i in s:
            i[0] = ru_name.get(i[0])
            file1_obj.write(f'{list_to_str(i)}\n')
