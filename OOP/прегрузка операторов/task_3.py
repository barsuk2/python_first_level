class Cell:
    def __init__(self, quantity):
        if  not isinstance(quantity,int):
            print(f'ошибка типа: {type(quantity)}')
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if abs(self.quantity - other.quantity) != 0:
            return Cell(abs(self.quantity - other.quantity))
        else:
            return 'ошибка вычитания клеток'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity // other.quantity)
        elif self.quantity < other.quantity:
            return Cell(other.quantity // self.quantity)
        else:
            return 'ошибка деления клеток'

    def make_order(self, quant):
        count = 0
        for i in range(self.quantity):
            print('*', end='')
            count += 1
            if count == quant:
                print('\n')
                count = 0

    def __str__(self):
        return f'{self.quantity}'


cell_1 = Cell(20)
cell_2 = Cell(10)
cell_3 = Cell(3)

print((cell_1 + cell_2) * cell_3)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
cell_1.make_order(5)
