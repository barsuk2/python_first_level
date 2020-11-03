class Auto:
    numInstances = 0

    # @staticmethod
    def __init__(self):
        Auto.numInstances = Auto.numInstances + 1

    def print_num_instances(self):
        print(f'{Auto.numInstances}')


# a, b, c, = Auto(), Auto(), Auto()
#
# a.print_num_instances()
# Auto().print_num_instances()


class Methods:
    def imeth(self, x):  # Обычный метод экземпляра
        print(self, x)

    def smeth(x):  # Статический метод: экземпляр не передается
        print(x)

    def cmeth(cls, x):  # Метод класса: получает класс, но не экземпляр
        print(cls, x)

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)


class M(Methods):
    pass


# obj = Methods()
# Methods.smeth(10)
# obj.smeth(10)
# Methods.cmeth(5)
# M.cmeth(5)


class Spam:
    intInstances = 0

    def count(cls):
        cls.intInstances += 1

    def __init__(self):
        self.count()


class Sub1(Spam):
    # intInstances = 0

    def __init__(self):
        Spam.__init__(self)


class Sub2(Spam):
    intInstances = 0


a = Spam()
a1 = Spam()
b1, b2 = Sub1(), Sub1()

c1, c2, c3 = Sub2(), Sub2(), Sub2()

print(a.intInstances, a1.intInstances)
print(b1.intInstances)
print(c1.intInstances)
