'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

import random


class Car:
    def __init__(self, speed, color, name, is_police=False):  # is_police булево
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_class_name()

    def show_class_name(self):
        print('Car - class')

    def go(self):
        if self.speed > 0:
            return self.speed
        else:
            return self.speed

    def stop(self):
        if self.speed == 0:
            return f'Машина стоит'
        else:
            return f'Машина не стоит'

    @staticmethod
    def turn():  # направление поворота
        direction = random.choice(['left', 'right', 'rear', 'forward'])
        return direction

    def show_speed(self):
        return self.speed
        # print(f'Текущая скорость {self.speed}')



class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_class_name(self):
        print('TownCar - class')

    def show_speed(self):
        speed = self.speed if self.speed < 60 else f'Вы превысили скорость на {self.speed - 60:.02f} км/ч'
        return speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_class_name(self):
        print('SportCar - class')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_class_name(self):
        print('WorkCar - class')

    def show_speed(self):
        speed = self.speed if self.speed < 40 else f'Вы превысили скорость на {self.speed - 40:.02f} км/ч'
        return speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=True)

    def show_class_name(self):
        print('PoliceCar - class')

c = Car(0, 'red', 'bugatty')
print('С какой скорость машина двигается', c.go())
print('Текущая скорость', c.show_speed())
print('Это полиция? ', c.is_police)
print('куда едем? - ', c.turn())
print()

t = TownCar(65, 'gray', 'Mazda', False)
print('С какой скорость машина двигается', t.go())
print('Текущая скорость', t.show_speed())
print('Это полиция? ', t.is_police)
print('куда едем? - ', t.turn())
print()

s = SportCar(250, 'White and Black', 'Mazeratty', True)
print('С какой скорость машина двигается', s.go())
print('Текущая скорость', s.show_speed())
print('Это полиция? ', s.is_police)
print('куда едем? - ', s.turn())
print()

w = WorkCar(40.1, 'White and Black', 'Mazeratty', True)
print('С какой скорость машина двигается', w.go())
print('Текущая скорость', w.show_speed())
print('Это полиция? ', w.is_police)
print('куда едем? - ', w.turn())
print()

p = PoliceCar(265, 'White and Blue', 'Maclaren')
print('С какой скорость машина двигается', p.go())
print('Текущая скорость', p.show_speed())
print('Это полиция? ', p.is_police)
print('куда едем? - ', p.turn())
print()