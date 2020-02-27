'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    _income = {"wage": 50000, "bonus": 10000}  # оклад и премия

    def __init__(self, wname, wsurname, wposition):
        self.name = wname
        self.surname = wsurname
        self.position = wposition
        # self._income = {"wage": 50000, "bonus": 10000}  # оклад и премия

    def values(self):
        return self.name, self.surname, self.position, Worker._income


class Position(Worker):
    def __init__(self, wname, wsurname, wposition):
        super().__init__(wname, wsurname, wposition)
        self.get_full_name()

    def get_full_name(self):
        return (f'Полное имя работника: {self.name} {self.surname}')

    def get_total_income(self):
        res = float()
        for x, y in Position._income.items():
            res += y
        return (f'Полный оклад - {res}')


p = Position('Иван', 'Петрович', 'Слесарь')
print(p.get_full_name())
print(p.get_total_income())
