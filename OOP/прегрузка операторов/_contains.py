class Basket:
    """Пример использования  __contains__ для проверки вхождения тип A in d"""
    def __init__(self):
        self.items = []

    def add(self, buy):
        self.items.append(buy)

    def __getitem__(self, item):
        print(f'get[{item}]:', end='')
        return self.items[item].upper()

    def __contains__(self, item):
        print('contains ', end='')
        return item in self.items


class_1 = Basket()
class_1.add('приобретение')
class_1.add('реализация')
class_1.add('покупательский')

print('покупательский' in class_1)
