import copy


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        resilt = []
        for elem in self.matr:
            elem = map(str, elem)
            resilt.append(' '.join(elem))
        resilt = "\n".join(resilt)
        return f'{resilt}'

    def __add__(self, other):
        """Столкнулся с тем, что операции копирования mylist = self.matr.copy() и
        mylist = self.matr[:] не работают, значения self.matr после выполнения метода __add__
        меняет значение на матрицу сыммы. Прошу на занятии дать комментарий"""
        # my_list = self.matr.copy() # пример с измением значения self.matr
        my_list = copy.deepcopy(self.matr)
        if self.len_matrix == other.len_matrix:
            for i in range(len(my_list)):
                for j in range(len(my_list[0])):
                    my_list[i][j] = my_list[i][j] + other.matr[i][j]
            return Matrix(my_list)
        else:
            return 'размерность матриц разная'

    @property
    def len_matrix(self):
        return [len(self.matr), len(self.matr[0])]


matrica_1 = Matrix([[1, 2, 1], [3, 4, 2], [1, 2, 2]])
matrica_2 = Matrix([[2, 4, 2], [1, 1, 2], [2, 3, 2]])

matrica_3 = Matrix([[2, 4, 2, 1, 2, 2], [2, 3, 2, 1, 2, 4]])
matrica_4 = Matrix([[6, 4, 3, 4, 5], [6, 5, 4, 3, 1]])

print(f'{matrica_1}\n')
print(f'{matrica_2}\n')

d = matrica_1 + matrica_2
print('')
print(f'сумма \n{d}\n')
# print(type(d))
d = d + matrica_2
print(f'сумма \n{d}\n')
print(f'{matrica_1}\n')

print(f'{matrica_3}\n')
print(f'{matrica_4}\n')
d = matrica_3 + matrica_4
print(f'сумма \n{d}\n')

