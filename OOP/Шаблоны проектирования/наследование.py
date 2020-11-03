class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def give_raise(self,persent):
        self.salary *= (1+persent/100)
        return self.salary
    def work(self):
        print(self.name,'- разнорабочий')
    def __repr__(self):
        return f'Employee: {self.name}, salary = {self.salary}'


class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name, 50000)

    def work(self):
        print(self.name,'- повар')

class Server(Employee):
    def __init__(self,name):
        super().__init__(self,name, 30000)

    def work(self):
        print(self.name,'- interfaces with castemer')


class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'- makes pizza')


r_bob = PizzaRobot('bob')
print(r_bob)

r_bob.work()
r_bob.give_raise(20)
print(r_bob)
print()

for kalss in Employee, Chef, PizzaRobot:
    obj =kalss(kalss.__name__)
    obj.work()