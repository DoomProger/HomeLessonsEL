'''
 *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
 В кортеже должно быть два элемента — номер товара и словарь с параметрами
 (характеристиками товара: название, цена, количество, единица измерения).
 Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''

goods_sctucture = []
dict_characteritic = {}
a = tuple()
item = 1

keys = ['название', 'цена', 'количество', 'eд']

while True:
    end = input('Вводим?')
    if end != '':
        goods_name = input('Введите название товара: ')
        goods_price = float(input('Введите цену товара: '))
        goods_count = int(input('Введите количество: '))
        goods_item = input('Введите единицу измерения (шт., кг): ')
        dict_characteritic = {keys[0]: goods_name, keys[1]: goods_price, keys[2]: goods_count, keys[3]: goods_item}
        goods_sctucture.append(tuple([item, dict_characteritic]))
        item += 1
    else:
        break
for good in goods_sctucture:
    print(good)

dict_analytic = {}
list_name = []
list_price = []
list_count = []
list_item = []

for i in goods_sctucture:
    list_name.append(i[1].setdefault(keys[0]))
    list_price.append(i[1].setdefault(keys[1]))
    list_count.append(i[1].setdefault(keys[2]))
    list_item.append(i[1].setdefault(keys[3]))

dict_analytic = {keys[0]: list_name, keys[1]: list_price, keys[2]: list_count, keys[3]: list_item}
print('')
print(dict_analytic)
