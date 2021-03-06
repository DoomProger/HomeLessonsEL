'''
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

'''

class Road:

    def __init__(self, len_road, width_road):
        Road._length = len_road
        Road._width = width_road

    def mass_asfalt(self):
        mass = 25
        depth = 1
        depth_num_roadbed = 5
        result = (Road._length * Road._width * mass * (depth * depth_num_roadbed)) / 1000
        return result


r = Road(20, 5000)
print('Для покрытия одного кв метра дороги асфальтом нужно {} т. асфальта'.format(r.mass_asfalt()))

