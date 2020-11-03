class GetItemAndSetItem:
    """Доступ добавление по индексу"""
    def __init__(self):
        self.list = [2,5,55]

    def __getitem__(self, item):
        return self.list[:item]

    def __setitem__(self, key, value):
        self.list[key] = value

class A:
    """ Итерация с getitem"""
    def __init__(self, date, date2):
        self.date = date
        self.date2 = date2
    def __getitem__(self, item):
        return self.date[item],  self.date2[item]

a =A('Gell','qwe')

for i in a:
    print(i)