class Road:
    def __init__(self, width=0, length=0):
        self._width = width
        self._length = length

    def result_mass(self, massa_na_sm, depth):
        return self._length * self._width * massa_na_sm * depth / 1000

    def setter(self, width, length):
        self._width = width
        self._length = length


road1 = Road()
road1.setter(20, 5000)
print(road1.result_mass(25, 5))
