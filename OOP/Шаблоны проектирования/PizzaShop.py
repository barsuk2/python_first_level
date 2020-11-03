class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, persent):
        self.salary *= (1 + persent / 100)
        return self.salary

    def work(self):
        print(self.name, '- разнорабочий')

    def __repr__(self):
        return f' [Employee: {self.name}, salary = {self.salary}]'


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, '- повар')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 30000)

    def work(self):
        print(self.name, '- interfaces with castemer')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, '- makes pizza')


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        return print(self.name, 'order from', server)

    def pay(self, server):
        return print(self.name, 'pays for item to', server)

class Oven:
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = Chef('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.oven = Oven()
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


scene = PizzaShop()
scene.order('Homer')
print('....')
scene.order('shaggy')