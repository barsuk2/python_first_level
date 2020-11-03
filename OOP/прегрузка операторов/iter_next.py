class BasketIter:
    def __init__(self,series):
        self.series  = series
        self._ind = 0

    def __next__(self):
        if self._ind < len(self.series):
            self._ind += 1
            return self.series[self._ind -1]
        raise  StopIteration


class Basket:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        # return (el for el in self._items)  # next()
        return BasketIter(self._items)


basket_1 = Basket()
basket_1.add('iPhone 11')
basket_1.add('iPad Pro')
basket_1.add('Galaxy S20')

for el in basket_1:
    print(el)