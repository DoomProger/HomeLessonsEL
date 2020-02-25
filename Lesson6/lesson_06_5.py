'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print('Запуск отрисовки')
        pass


class Pen(Stationery):
    def draw(self):
        print('Йа ручка')

class Pencil(Stationery):
    def draw(self):
        print('Йа карандаш')

class Handle(Stationery):
    def draw(self):
        print('Йа маркер')

s = Stationery('Название')
print(s.title)

p = Pen('Ручка')
print(p.title)

pe = Pencil('Карандаш')
print(pe.title)

h = Handle('Маркер')
print(h.title)
