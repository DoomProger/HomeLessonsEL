'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = list(matrix_list)
        # print(self.matrix_list)

    def __str__(self):
        a = self.matrix_list
        eli1 = ''
        for i in a:
            eli = ''
            for el in i:
                eli += str(f'|{el}|')
            eli1 += f'{eli}\n'
        return f'{eli1}'

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
            res = []
            for lel in zip(self.matrix_list, other.matrix_list):
                tmp = []
                for num in zip(lel[0], lel[1]):
                    tmp.append(sum(num))
                res.append(tmp)

            eli1 = ''
            for i in res:
                eli = ''
                for el in i:
                    eli += str(f'|{el}|')
                eli1 += f'{eli}\n'
            return f'result matrix is\n{eli1}'
        else:
            return 'Матрицы не равны'


aa = [[5, 8], [1, 4], [7, 1]]
cc = [[1, 3], [2, 6], [2, 9]]

matr1 = Matrix(aa)
matr2 = Matrix(cc)

print(matr1)
print(matr2)

print(matr1 + matr2)
