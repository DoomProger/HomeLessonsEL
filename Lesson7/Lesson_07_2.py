'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

# пальто - coat
# костюм - suit
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def sum_volume_cloth(self):
        pass


class SumClothes(Clothes):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def volume_coat(self):
        cloth = self.size / 6.5 + 0.5
        return cloth

    def volume_suit(self):
        cloth = 2 * self.height + 0.3
        return cloth

    def sum_volume_cloth(self):
        result = self.volume_coat() + self.volume_suit()
        return result


otezhta = SumClothes(123, 222)
print(f'Нужно ткани на костюм {otezhta.volume_suit():.02f}, при росте {otezhta.height}')
print(f'Нужно ткани на пальто {otezhta.volume_coat():.02f}, при размере {otezhta.size}')
print(f'Всего ткани нужно: {otezhta.sum_volume_cloth():.02f}')