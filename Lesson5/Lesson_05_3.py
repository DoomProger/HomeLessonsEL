'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''


def average(ls):
    return sum(ls) / len(ls)


with open('lesson_05_3_avgincomestaff.txt', encoding='utf-8') as file_obj:
    # a =[]
    lf = [line.split() for line in file_obj]

    for i in lf:
        if int(i[1]) < 20000:
            print('Получает меньше 20 тыс. - ', i[0])

    zp = [int(a[1]) for a in lf]
    print('Среедняя ЗП', average(zp))






    # print(file_obj.read())
    #
    # input('continue?')
    # print([x for x in enumerate(file_obj)])
    # a = [x for x in enumerate(file_obj)]
    # print(a)
    # a = [line.split() for line in file_obj]
    # print(a)
    # print(map(enumerate, a))
    # print([i for i in a if int(i[1]) < 20000])
    # print(sum(i[1]) for i in a)

    # for i in a:
    #     print('i-', i[1])

'''
    for line in file_obj:
        # print(f'Количество {list(line.split())}')
        # print([x for x in enumerate(list(line.split())) if int(x[1]) < 20000])
        # input('--')
        # print(line.strip())
        # print([x for x in enumerate(list(line.split()))])
        # print([x for x in enumerate(list(line.split())) if x.index(1)[1] < 20000])
        # a = [x for x in enumerate(list(line.split())) if int(x[1][1]) < 20000]
        # a = [x for y, x in enumerate(list(line.split()))]
        list_my = list(line.split())
        print('some', list(line.split()))
        a = [x for x in enumerate(list_my) if int(x[1][1]) > 15]
        print('->', a)
        print(a[1][1])
        input('cont')
'''
