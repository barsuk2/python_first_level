from abc import ABC, abstractmethod

class AbstractTotalTextile(ABC):
    @abstractmethod
    def total_textile(self):
        pass



class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Clothes:

    def __init__(self, name):
        self.name = name




class Coat(Clothes,AbstractTotalTextile):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def total_textile(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes,AbstractTotalTextile):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def total_textile(self):
        return 2 * self.height + 0.3


class Production:
    ''' Класс производство одежды'''
    unit = 'метр'
    def __init__(self, user):
        self.user = user
        self.priducts = []

    def add(self, product):
        self.priducts.append(product)

    def sum_price(self):
        return sum((el.total_textile for el in self.priducts))
    def __len__(self):
        return len(self.priducts)

user = User('Павел')
coat2 = Coat('Бушлат морской черный', 20)
coat3 = Coat('Бушлат морской черный', 10)
cost1 = Costume('Костюм синий в белую полоску', 20)
production_1 = Production(user)
production_1.add(coat2)
production_1.add(coat2)
production_1.add(coat2)
production_1.add(coat2)
production_1.add(coat2)
production_1.add(coat2)
production_1.add(cost1)
production_1.add(cost1)
production_1.add(cost1)
production_1.add(cost1)
production_1.add(cost1)


print(f'Для пользователя {production_1.user} сформирован заказ на производство.\nНа {len(production_1)} едениц продукции неоходимо {production_1.sum_price():.2f} '
      f'{production_1.unit}ов(а) ткани')