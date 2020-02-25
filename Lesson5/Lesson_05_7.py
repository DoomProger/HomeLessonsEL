'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
firm_dict = {}
ave_pof_dict = {}
average_profit = 0
i = 0
# прибыль = выручка - издержки

with open('lesson_05_7_firmdata.txt', encoding='utf8') as file_firm:
    # print(len(file_firm.readlines()))
    for s in file_firm:
        firm_list = list(s.split())
        profit = int(firm_list[2]) - int(firm_list[3])
        if profit > 0:
            i += 1
            average_profit += profit
        print(average_profit)
        firm_dict.update({firm_list[0]: profit})
    ave_pof_dict.update({'average_profit': average_profit / i})
    json_obj = [firm_dict, ave_pof_dict]

with open('lesson_05_7_firmdata.json', 'w', encoding='utf8') as js_f:
    json.dump(json_obj, js_f, ensure_ascii=False)

